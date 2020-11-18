from pathlib import Path

import streamlit as st

import numpy as np
import pandas as pd
import glob

st.title("Let's visualize the versionned experiments")
metrics = glob.glob('**/square_err.metric', recursive=True)

df = pd.DataFrame({
    'xp': [Path(metric).parent for metric in metrics],
    'square_error': [float(Path(metric).read_text()) for metric in metrics],
})

df

st.write("Select an experiment to plot against the target : ")

option = st.selectbox(
    'Choose experiment branch',
     df['xp'],
    format_func=lambda p: p.name or 'working dir'
)

'You selected: ', option

target = np.load('target.npy')
out = np.load(option / 'out.npy')
plot_data = pd.DataFrame(
    {
        'target': target,
        'out': out
    }
)
st.line_chart(plot_data)