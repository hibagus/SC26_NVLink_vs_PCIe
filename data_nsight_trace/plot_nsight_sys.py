# (C) 2026 Bagus Hanindhito, Dell Technologies/The University of Texas at Austin

#%% Import Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse
import os

def parse_args(args_list=None):
    parser = argparse.ArgumentParser(description="Parse and Plot Nsight Systems Data into Timeline")
    parser.add_argument(
        "--directory",
        type=str,
        default="./",
        help="The location of the data from Nsight Systems"
    )
    return parser.parse_args(args_list)


def parse_and_plot(title,input_name,output_name):
    
    # Open Tab-Seprated-File
    df=pd.read_csv(input_name, sep='\t',usecols=[0, 1, 2])

    # Remove s on Start and convert to numeric fp64
    df['Start_s'] = df['Start'].str.replace('s','').astype('float64')

    # Split the number and unit
    split_duration = df['Duration'].str.split(' ', expand=True)
    df[['Duration_Value', 'Duration_Unit']] = split_duration
    df['Duration_Value'] = df['Duration_Value'].astype('float64')

    # Convert duration to second
    df['Duration_s'] = np.where(df['Duration_Unit'] == 'ms', df['Duration_Value'] / 1000,
                       np.where(df['Duration_Unit'] == 'μs', df['Duration_Value'] / 1000000,
                       np.where(df['Duration_Unit'] == 'ns', df['Duration_Value'] / 1000000000, df['Duration_Value'])))

    # sort by Start_s
    df = df.sort_values(by='Start_s').reset_index(drop=True)

    # Clean-up Kernel Name from Duration
    df['Name_Cleaned'] = df['Name'].str.replace(r'\s*\[[^\]]*\]$', '', regex=True)

    # Grouping kernel

    # NVIDIA Myelin
    df.loc[df['Name_Cleaned'].str.contains('__myl'), 'Group'] = 'TRT-Myelin'
    df.loc[df['Name_Cleaned'].str.contains('myelin'), 'Group'] = 'TRT-Myelin'
    
    # NCCL 
    df.loc[df['Name_Cleaned'].str.contains('ncclAllReduce'), 'Group'] = 'ncclAllReduce'
    df.loc[df['Name_Cleaned'].str.contains('ncclAllGather'), 'Group'] = 'ncclAllGather'
    df.loc[df['Name_Cleaned'].str.contains('ncclSend'), 'Group'] = 'ncclSend'
    df.loc[df['Name_Cleaned'].str.contains('ncclRecv'), 'Group'] = 'ncclRecv'
    
    df.loc[df['Name_Cleaned'].str.contains('ncclDevKernel_AllReduce'), 'Group'] = 'Kernel-nccl'
    df.loc[df['Name_Cleaned'].str.contains('ncclDevKernel_AllGather'), 'Group'] = 'Kernel-nccl'
    df.loc[df['Name_Cleaned'].str.contains('ncclDevKernel_SendRecv'), 'Group'] = 'Kernel-nccl'
    
    # TensorRT LLM
    df.loc[df['Name_Cleaned'].str.contains('ExecutionContext::enqueue'), 'Group'] = 'TRT-Batch'
    df.loc[df['Name_Cleaned'].str.contains('tensorrt_llm::kernels'), 'Group'] = 'TRT-Kernel'
    df.loc[df['Name_Cleaned'].str.contains('tensorrt_llm::runtime'), 'Group'] = 'TRT-Runtime'
    
    # Multi-Head Attention
    df.loc[df['Name_Cleaned'].str.contains('fmha_v2_flash'), 'Group'] = 'Kernel-MultiHead-Attention'
    df.loc[df['Name_Cleaned'].str.contains('kernel_mha'), 'Group'] = 'Kernel-MultiHead-Attention'
    
    # cuDNN GEMM
    df.loc[df['Name_Cleaned'].str.contains('xmma_gemm'), 'Group'] = 'Kernel-GEMM-CUBLAS'
    
    # cutlass GEMM
    df.loc[df['Name_Cleaned'].str.contains('cutlass::gemm'), 'Group'] = 'Kernel-GEMM-CUTLASS'
    
    # Llama Layer
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('mlp/proj'), 'Group'] = 'LlaMA-MLP'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('mlp/fc_gate_plugin'), 'Group'] = 'LlaMA-MLP'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('attention/dense'), 'Group'] = 'LlaMA-Attention'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('attention/wrapper'), 'Group'] = 'LlaMA-Attention'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('attention/qkv'), 'Group'] = 'LlaMA-Attention'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('post_layernorm'), 'Group'] = 'LlaMA-Norm'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('transformer/vocab_embedding'), 'Group'] = 'LlaMA-Embedding'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('lm_head'), 'Group'] = 'LlaMA-Head'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('recv'), 'Group'] = 'LlaMA-Receive'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('send'), 'Group'] = 'LlaMA-Send'
    df.loc[df['Name_Cleaned'].str.contains('LLaMAForCausalLM') & df['Name_Cleaned'].str.contains('PWN'), 'Group'] = 'LlaMA-Other'
    
    # Memcpy
    df.loc[df['Name_Cleaned'].str.contains('Memcpy HtoD'), 'Group'] = 'Mem-Memcpy-H2D'
    df.loc[df['Name_Cleaned'].str.contains('Memcpy DtoH'), 'Group'] = 'Mem-Memcpy-D2H'
    df.loc[df['Name_Cleaned'].str.contains('Memcpy DtoD'), 'Group'] = 'Mem-Memcpy-D2D'
    df.loc[df['Name_Cleaned'].str.contains('Memset'), 'Group'] = 'Mem-Memset'
    
    # Other Kernels
    df.loc[df['Name_Cleaned'].str.contains('genericReformat'), 'Group'] = 'Kernel-Data-Reformat'
    
    # Missing Group
    if df['Group'].isna().sum()>0:
        print("WARNING!: There are some events that do not have group assigned. They will not be plotted")
        print(df.loc[df['Group'].isna(),'Name_Cleaned'])


    # Cumulative Sum of Start and Duration, to take care of the entry where Start is the same due to precision loss.
    df['Shifted'] = df.groupby(['Group','Start_s'])['Duration_s'].shift().fillna(0)
    df['Start_Offset'] = df.groupby(['Group','Start_s'])['Shifted'].cumsum()

    # Adjusted Start 
    df['Start_s_adjusted'] = df['Start_s'] + df['Start_Offset']

    if df['Start_s_adjusted'].min() > 30:
        df['Start_s_adjusted'] = df['Start_s_adjusted'] - 20
    
    #%% Color Library
    color = { 'Kernel-GEMM-CUBLAS'           : '#157CBF',
              'Kernel-GEMM-CUTLASS'          : '#8BB84B',
              'Kernel-MultiHead-Attention'   : '#5B3C89',
              'Kernel-Data-Reformat'         : '#F58634',
              'Kernel-nccl'                  : '#ED3237',
    
              'ncclAllReduce'         : '#F58634',
              'ncclAllGather'         : '#A8518A',
              'ncclSend'              : '#3E4095',
              'ncclRecv'              : '#00A859',
              
              'TRT-Batch'             : '#ED3237',
              'TRT-Kernel'            : '#00A859',
              'TRT-Runtime'           : '#3E4095',
              'TRT-Myelin'            : '#A8518A',
              
              'Mem-Memcpy-H2D'        : '#9D98CA',
              'Mem-Memcpy-D2H'        : '#9DD3AF',
              'Mem-Memcpy-D2D'        : '#F7ADAF',
              'Mem-Memset'            : '#73B9E6',
              
              'LlaMA-MLP'             : '#5CC6D0',
              'LlaMA-Attention'       : '#A793C5',
              'LlaMA-Norm'            : '#9DD3AF',
              'LlaMA-Embedding'       : '#FAD2E3',
              'LlaMA-Head'            : '#FFCC29',
              'LlaMA-Send'            : '#3E4095',
              'LlaMA-Receive'         : '#00A859',
              'LlaMA-Other'           : '#373435'
    }
    # Broken Barh Plot Drawing
    fig, ax = plt.subplots()
    fig.set_figwidth(24) 
    #fig.set_figheight(6) 
    
    yticklabels=[]
    ytick=[]
    
    for i, (category, group) in enumerate(df.groupby('Group')):
        xranges = [(row['Start_s_adjusted'], row['Duration_s']) for _, row in group.iterrows()]
        yrange = (i * 10, 6)  # Adjust y-position and height for each category
        ax.broken_barh(xranges, yrange, facecolors=color[category], label=category)
        yticklabels.append(category)
        #print(category)
        ytick.append(i * 10 + 3)
    
    ax.set_yticks(ytick) # Set y-tick positions
    ax.set_yticklabels(yticklabels) # Set y-tick labels
    ax.set_xlabel('Time (s)')
    ax.set_title(title)
    #ax.legend()    
    
    plt.xlim(20.0, 20.8)
    plt.xticks(np.arange(20.0, 20.8, 0.1))

    #plt.axvline(x=20.0, color='r', linestyle='--', label='Vertical Line')
    
    plt.savefig(output_name, format='pdf')
    #plt.show()


def main(args_list=None):
    args = parse_args(args_list)

    # Full Path Directory
    work_directory = os.path.abspath(args.directory)
    print("Using " + work_directory + " as working directory...")
    
    # List of available file to plot in the directory
    compatible_files = ['GPU0_19', 'GPU1_3B', 'GPU2_4C', 'GPU3_5D', 'GPU4_9B', 'GPU5_BB', 'GPU6_CB', 'GPU7_DB']

    list_all_files = os.listdir(work_directory)
    list_compatible_files = list(set(list_all_files) & set(compatible_files))
    
    if(len(list_compatible_files)==0):
        print("No compatible files detected. Exiting...")
        exit(-1)
    
    print(list_compatible_files)
    
    # Plot every compatible file in the list
    for compatible_file in list_compatible_files:
        print("Parsing and plotting file " + compatible_file)
        file_path = os.path.join(work_directory, compatible_file)
        title = args.directory + "-" + compatible_file
        output_plot = file_path+".pdf"
        print(output_plot)
        parse_and_plot(title, file_path, output_plot)

if __name__ == "__main__":
    main()












