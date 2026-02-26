bundle:
  name: my-data-project

# Global variables
variables:
  catalog:
    description: autoloader
  schema:
    description: source_data

targets:
  dev:
    default: true
    variables:
      catalog: autoloader
      schema: source_data

  prod:
    variables:
      catalog: autoloader
      schema: source_data

resources:
  jobs:
    my_job:
      name: my-data-job

      tasks:
        - task_key: main_task
          python_wheel_task:
            package_name: my_data_project
            entry_point: main
          environment_key: default

      # ⭐ THIS MAKES IT SERVERLESS
      environments:
        - environment_key: default
          spec:
            client: "1"
            dependencies:
              - .

      parameters:
        - name: catalog
          default: ${var.catalog}
        - name: schema
          default: ${var.schema}