from app.metric_router.dto import MetricData


def get_metric(id: int) -> MetricData:
    return MetricData(
        id=id,
        name="Productivity",
        value=100,
    )
