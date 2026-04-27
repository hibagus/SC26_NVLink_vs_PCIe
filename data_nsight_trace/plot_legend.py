import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse
import os


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

categories = list(color.keys())
values = list(color.values())
values = [1] * len(values)

bar_colors = [color[cat] for cat in categories]

fig, ax = plt.subplots()

ax.bar(categories, values, color=bar_colors)
fig.set_figheight(20) 

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Custom Colors')
plt.xticks(rotation=90)

plt.savefig('legend.pdf', format='pdf')
plt.show()