import torch
import plotly as plt


def plot_samples(samples, num=8, rows=2, cols=4):
    fig = plt.subplots.make_subplots(
        rows=rows,
        cols=cols,
        specs=[[{"type": "Scatter3d"} for _ in range(cols)] for _ in range(rows)],
    )
    indices = torch.randperm(samples.size(0))[:num]
    for i, sample in enumerate(samples[indices].cpu()):
        fig.add_trace(
            plt.graph_objects.Scatter3d(
                x=sample[:, 0],
                y=sample[:, 2],
                z=sample[:, 1],
                mode="markers",
                marker=dict(size=3, opacity=0.8),
            ),
            row=i // cols + 1,
            col=i % cols + 1,
        )
    fig.update_layout(showlegend=False)
    return fig
