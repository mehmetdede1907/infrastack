import sentry_sdk

sentry_sdk.init(
    dsn="__DSN__",
    traces_sample_rate=1.0,
    # set the instrumenter to use OpenTelemetry instead of Sentry
    instrumenter="otel",
)
