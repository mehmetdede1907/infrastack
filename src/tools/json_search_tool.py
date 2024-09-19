from crewai_tools import JSONSearchTool

class EnhancedJSONSearchTool:
    def __init__(self):
        self.log_tool = JSONSearchTool(json_path='./data/logs.json')
        self.metric_tool = JSONSearchTool(json_path='./data/metrics.json')
        self.trace_tool = JSONSearchTool(json_path='./data/traces.json')

    def search_logs(self, query):
        return self.log_tool.run(query)

    def search_metrics(self, query):
        return self.metric_tool.run(query)

    def search_traces(self, query):
        return self.trace_tool.run(query)

json_search_tool = EnhancedJSONSearchTool()