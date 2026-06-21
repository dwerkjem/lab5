import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def seminar_plots(companies: list[dict]) -> None:
    """Creates seminar charts on one page."""
    df = pd.DataFrame(companies)

    if df.empty:
        print("No company data to plot.")
        return

    attendee_counts = df["Attendees"].value_counts().sort_index().reset_index()

    attendee_counts.columns = ["Attendees", "Company Count"]

    scatter_fig = px.scatter(
        df,
        x="Attendees",
        y="Cost",
        color="Cost bracket",
        hover_name="Company Name",
        text="Company Name",
    )

    pie_fig = px.pie(
        df,
        names="Company Name",
        values="Attendees",
    )

    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[
            [{"type": "xy"}, {"type": "domain"}],
            [{"type": "xy", "colspan": 2}, None],
        ],
        subplot_titles=(
            "Company Cost by Attendees",
            "Seats Taken by Each Company",
            "How Often Each Group Size Was Reserved",
        ),
        row_heights=[0.55, 0.45],
        vertical_spacing=0.18,
    )

    for trace in scatter_fig.data:
        fig.add_trace(trace, row=1, col=1)

    for trace in pie_fig.data:
        fig.add_trace(trace, row=1, col=2)

    fig.add_trace(
        go.Bar(
            x=attendee_counts["Attendees"],
            y=attendee_counts["Company Count"],
            text=attendee_counts["Company Count"],
            textposition="outside",
            name="Company count",
        ),
        row=2,
        col=1,
    )

    fig.update_traces(
        textposition="top center",
        marker_size=10,
        selector=dict(type="scatter"),
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        selector=dict(type="pie"),
    )

    fig.update_xaxes(title_text="Attendees", row=1, col=1)
    fig.update_yaxes(title_text="Cost", row=1, col=1)

    fig.update_xaxes(
        title_text="Number of attendees reserved",
        dtick=1,
        row=2,
        col=1,
    )

    fig.update_yaxes(
        title_text="Number of companies",
        dtick=1,
        row=2,
        col=1,
    )

    fig.update_layout(
        title_text="Computer Haven Seminar Registration Charts",
        showlegend=True,
        height=850,
    )

    fig.show()
