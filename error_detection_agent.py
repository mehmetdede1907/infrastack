# error_detection_agent.py

from crewai import Agent
from data.mock import logs
from data.mock import metrics
from data.mock import traces
class ErrorDetectionAgent(Agent):
    def __init__(self):
        super().__init__(name="ErrorDetectionAgent")

    def run(self):
        # Detect errors in logs, metrics, and traces
        error_logs = self.detect_errors_in_logs(logs)
        error_metrics = self.detect_errors_in_metrics(metrics)
        error_traces = self.detect_errors_in_traces(traces)

        # Aggregate detected errors
        detected_errors = {
            'logs': error_logs,
            'metrics': error_metrics,
            'traces': error_traces
        }

        return detected_errors

    def detect_errors_in_logs(self, logs):
        error_logs = []
        for log in logs:
            if log['severity'] == 'ERROR':
                error_logs.append(log)
        return error_logs

    def detect_errors_in_metrics(self, metrics):
        error_metrics = []
        for metric_entry in metrics:
            for metric in metric_entry['metrics']:
                if 'error' in metric['name'].lower():
                    for data_point in metric['dataPoints']:
                        if data_point['value'] > 0:
                            error_metrics.append({
                                'timestamp': metric_entry['timestamp'],
                                'metric_name': metric['name'],
                                'attributes': data_point['attributes'],
                                'value': data_point['value']
                            })
        return error_metrics

    def detect_errors_in_traces(self, traces):
        error_traces = []
        for trace in traces:
            for span in trace['spans']:
                if 'status' in span and span['status']['code'] == 'ERROR':
                    error_traces.append({
                        'traceId': trace['traceId'],
                        'spanId': span['spanId'],
                        'name': span['name'],
                        'status': span['status'],
                        'attributes': span['attributes']
                    })
        return error_traces
