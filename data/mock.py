logs = [
    {
      "timestamp": "2023-10-01T12:00:05Z",
      "severity": "INFO",
      "body": "User successfully logged in.",
      "attributes": {
        "service.name": "auth-service",
        "user.id": "user_12345",
        "session.id": "session_abcde"
      }
    },
    {
      "timestamp": "2023-10-01T12:10:15Z",
      "severity": "INFO",
      "body": "Product list retrieved successfully.",
      "attributes": {
        "service.name": "product-service",
        "user.id": "user_12345",
        "product.count": 50
      }
    },
    {
      "timestamp": "2023-10-01T12:15:00Z",
      "severity": "ERROR",
      "body": "Request to /api/v1/checkout timed out.",
      "attributes": {
        "service.name": "checkout-service",
        "error.type": "TimeoutError",
        "error.message": "Operation timed out after 30 seconds",
        "http.method": "POST",
        "http.url": "/api/v1/checkout",
        "user.id": "user_67890"
      }
    },
    {
      "timestamp": "2023-10-01T12:20:30Z",
      "severity": "INFO",
      "body": "User added item to cart.",
      "attributes": {
        "service.name": "product-service",
        "user.id": "user_12345",
        "product.id": "prod_98765"
      }
    },
    {
      "timestamp": "2023-10-01T12:30:45Z",
      "severity": "ERROR",
      "body": "Failed to process payment due to timeout.",
      "attributes": {
        "service.name": "payment-service",
        "error.type": "TimeoutError",
        "error.message": "Payment gateway did not respond in time",
        "transaction.id": "txn_98765",
        "amount": 99.99,
        "currency": "USD"
      }
    },
    {
      "timestamp": "2023-10-01T12:45:10Z",
      "severity": "INFO",
      "body": "User successfully logged out.",
      "attributes": {
        "service.name": "auth-service",
        "user.id": "user_12345",
        "session.id": "session_abcde"
      }
    },
    {
      "timestamp": "2023-10-01T12:50:25Z",
      "severity": "ERROR",
      "body": "Database connection lost.",
      "attributes": {
        "service.name": "product-service",
        "error.type": "DatabaseError",
        "error.message": "Connection refused",
        "db.instance": "products_db",
        "db.host": "db-server-1"
      }
    },
    {
      "timestamp": "2023-10-01T13:00:00Z",
      "severity": "INFO",
      "body": "System health check passed.",
      "attributes": {
        "service.name": "health-monitor",
        "status": "All systems operational"
      }
    }
  ]

metrics = [
  {
    "timestamp": "2023-10-01T12:00:00Z",
    "metrics": [
      {
        "name": "cpu.usage",
        "unit": "percent",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "auth-service",
              "host.name": "server-1"
            },
            "value": 30.0
          },
          {
            "attributes": {
              "service.name": "product-service",
              "host.name": "server-2"
            },
            "value": 35.0
          }
        ]
      },
      {
        "name": "memory.usage",
        "unit": "percent",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "auth-service",
              "host.name": "server-1"
            },
            "value": 40.0
          },
          {
            "attributes": {
              "service.name": "product-service",
              "host.name": "server-2"
            },
            "value": 45.0
          }
        ]
      }
    ]
  },
  {
    "timestamp": "2023-10-01T12:15:00Z",
    "metrics": [
      {
        "name": "http.request.duration",
        "unit": "ms",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "checkout-service",
              "http.method": "POST",
              "http.status_code": "504"
            },
            "value": 30000
          }
        ]
      },
      {
        "name": "error.count",
        "unit": "1",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "checkout-service",
              "error.type": "TimeoutError"
            },
            "value": 1
          }
        ]
      }
    ]
  },
  {
    "timestamp": "2023-10-01T12:30:45Z",
    "metrics": [
      {
        "name": "http.request.duration",
        "unit": "ms",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "payment-service",
              "http.method": "POST",
              "http.status_code": "504"
            },
            "value": 30000
          }
        ]
      },
      {
        "name": "error.count",
        "unit": "1",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "payment-service",
              "error.type": "TimeoutError"
            },
            "value": 1
          }
        ]
      }
    ]
  },
  {
    "timestamp": "2023-10-01T12:50:25Z",
    "metrics": [
      {
        "name": "db.connection.errors",
        "unit": "1",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "product-service",
              "db.instance": "products_db"
            },
            "value": 1
          }
        ]
      },
      {
        "name": "cpu.usage",
        "unit": "percent",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "product-service",
              "host.name": "server-2"
            },
            "value": 80.0
          }
        ]
      }
    ]
  },
  {
    "timestamp": "2023-10-01T13:00:00Z",
    "metrics": [
      {
        "name": "cpu.usage",
        "unit": "percent",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "auth-service",
              "host.name": "server-1"
            },
            "value": 25.0
          },
          {
            "attributes": {
              "service.name": "product-service",
              "host.name": "server-2"
            },
            "value": 30.0
          }
        ]
      },
      {
        "name": "memory.usage",
        "unit": "percent",
        "dataPoints": [
          {
            "attributes": {
              "service.name": "auth-service",
              "host.name": "server-1"
            },
            "value": 35.0
          },
          {
            "attributes": {
              "service.name": "product-service",
              "host.name": "server-2"
            },
            "value": 40.0
          }
        ]
      }
    ]
  }
]

traces = [
  {
    "traceId": "trace-0001",
    "spans": [
      {
        "spanId": "span-0001",
        "parentSpanId": null,
        "name": "HTTP GET /api/v1/products",
        "kind": "SERVER",
        "startTime": "2023-10-01T12:10:15.000Z",
        "endTime": "2023-10-01T12:10:15.150Z",
        "attributes": {
          "service.name": "product-service",
          "http.method": "GET",
          "http.url": "/api/v1/products",
          "http.status_code": 200
        }
      },
      {
        "spanId": "span-0002",
        "parentSpanId": "span-0001",
        "name": "Database Query",
        "kind": "CLIENT",
        "startTime": "2023-10-01T12:10:15.050Z",
        "endTime": "2023-10-01T12:10:15.140Z",
        "attributes": {
          "db.system": "postgresql",
          "db.statement": "SELECT * FROM products LIMIT 100",
          "db.response_time_ms": 90
        }
      }
    ]
  },
  {
    "traceId": "trace-0002",
    "spans": [
      {
        "spanId": "span-0010",
        "parentSpanId": null,
        "name": "HTTP POST /api/v1/checkout",
        "kind": "SERVER",
        "startTime": "2023-10-01T12:15:00.000Z",
        "endTime": "2023-10-01T12:15:30.000Z",
        "status": {
          "code": "ERROR",
          "message": "TimeoutError"
        },
        "attributes": {
          "service.name": "checkout-service",
          "http.method": "POST",
          "http.url": "/api/v1/checkout",
          "http.status_code": 504
        }
      },
      {
        "spanId": "span-0011",
        "parentSpanId": "span-0010",
        "name": "Call Payment Service",
        "kind": "CLIENT",
        "startTime": "2023-10-01T12:15:00.050Z",
        "endTime": "2023-10-01T12:15:30.000Z",
        "status": {
          "code": "ERROR",
          "message": "TimeoutError"
        },
        "attributes": {
          "service.name": "checkout-service",
          "peer.service": "payment-service",
          "net.peer.ip": "192.168.1.20",
          "net.peer.port": 443
        }
      }
    ]
  },
  {
    "traceId": "trace-0003",
    "spans": [
      {
        "spanId": "span-0020",
        "parentSpanId": null,
        "name": "HTTP POST /api/v1/payment",
        "kind": "SERVER",
        "startTime": "2023-10-01T12:30:45.000Z",
        "endTime": "2023-10-01T12:31:15.000Z",
        "status": {
          "code": "ERROR",
          "message": "TimeoutError"
        },
        "attributes": {
          "service.name": "payment-service",
          "http.method": "POST",
          "http.url": "/api/v1/payment",
          "http.status_code": 504
        }
      },
      {
        "spanId": "span-0021",
        "parentSpanId": "span-0020",
        "name": "External Payment Gateway",
        "kind": "CLIENT",
        "startTime": "2023-10-01T12:30:45.050Z",
        "endTime": "2023-10-01T12:31:15.000Z",
        "status": {
          "code": "ERROR",
          "message": "TimeoutError"
        },
        "attributes": {
          "peer.service": "payment-gateway",
          "net.peer.ip": "203.0.113.10",
          "net.peer.port": 443
        }
      }
    ]
  },
  {
    "traceId": "trace-0004",
    "spans": [
      {
        "spanId": "span-0030",
        "parentSpanId": null,
        "name": "HTTP GET /api/v1/products",
        "kind": "SERVER",
        "startTime": "2023-10-01T12:50:25.000Z",
        "endTime": "2023-10-01T12:50:25.500Z",
        "status": {
          "code": "ERROR",
          "message": "DatabaseError"
        },
        "attributes": {
          "service.name": "product-service",
          "http.method": "GET",
          "http.url": "/api/v1/products",
          "http.status_code": 500
        }
      },
      {
        "spanId": "span-0031",
        "parentSpanId": "span-0030",
        "name": "Database Query",
        "kind": "CLIENT",
        "startTime": "2023-10-01T12:50:25.050Z",
        "endTime": "2023-10-01T12:50:25.490Z",
        "status": {
          "code": "ERROR",
          "message": "Connection refused"
        },
        "attributes": {
          "db.system": "postgresql",
          "db.statement": "SELECT * FROM products LIMIT 100",
          "db.instance": "products_db",
          "db.host": "db-server-1"
        }
      }
    ]
  }
]


  