from typing import Iterable, List, Optional, Tuple, Union
from typing_extensions import Self

import numpy as np
import plotly.graph_objects as go

from _base import (
    Knowledge,
    PlotlyBasePlotter
)


class DotPlotter(PlotlyBasePlotter):
    """Provides utilities for plotting dot plots."""

    def plot(
        self,
        content: Union[Knowledge, List[Tuple[float, float, str]]],
        topics: Optional[Iterable[str]] = None,
        top_n: Optional[int] = None,
        title: str = "Comparison of learner's subjects",
        x_label: str = "Subjects",
        y_label: str = "Mean",
        history: bool = False,
    ) -> Self:
        if isinstance(content, Knowledge):
            content = self._standardise_data(content, history, topics)

        content = content[:top_n]

        means = [lst[0] for lst in content]

        variances = [lst[1] for lst in content]

        titles = [lst[2] for lst in content]

        if history:
            timestamps = [lst[3] for lst in content]
            number_of_videos = []
            last_video_watched = []
            for timestamp in timestamps:
                number_of_videos.append(len(timestamp))
                last_video_watched.append(timestamp[-1])
        else:
            number_of_videos = [None for _ in variances]
            last_video_watched = [None for _ in variances]

        self.figure = go.Figure(data=go.Scatter(
            x=titles,
            y=means,
            marker=dict(
                size=50,
                cmax=max(means) + 0.001,
                cmin=min(means) - 0.001,
                color=means,
                colorbar=dict(
                    title="Means"
                ),
                colorscale="Greens"
            ),
            error_y=dict(type='data',
                         array=variances,
                         color='black',
                         thickness=4,
                         width=3,
                         visible=True),
            customdata=np.transpose([variances, number_of_videos, last_video_watched]),
            hovertemplate=self._hovertemplate(
                (
                    "%{x}",
                    "%{y}",
                    "%{customdata[0]}",
                    "%{customdata[1]}",
                    "%{customdata[2]}"
                ),
                history
            ),
            mode="markers"),
            layout=self._layout((title, x_label, y_label)))

        return self