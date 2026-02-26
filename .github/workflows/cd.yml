name: CD Pipeline

on:
  push:
    branches: [ main ]

jobs:

  # ---------------- DEV DEPLOY ----------------
  deploy-dev:
    runs-on: ubuntu-latest
    environment: dev

    steps:
      - uses: actions/checkout@v3

      # Install NEW Databricks CLI
      - name: Install Databricks CLI (NEW)
        run: |
          curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
          databricks -v

      # ⭐ Cache Terraform Provider (FIXES 503 ERROR)
      - name: Cache Terraform Providers
        uses: actions/cache@v3
        with:
          path: ~/.terraform.d/plugin-cache
          key: terraform-${{ runner.os }}-databricks

      # ⭐ Build Python Wheel (REQUIRED for python_wheel_task)
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Build Wheel
        run: |
          pip install --upgrade pip
          pip install wheel setuptools
          python setup.py bdist_wheel
          ls dist

      # Authenticate to Databricks
      - name: Configure Databricks Auth
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST_DEV }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN_DEV }}
        run: databricks current-user me

      # Validate bundle
      - name: Validate Bundle
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST_DEV }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN_DEV }}
        run: databricks bundle validate

      # Deploy to DEV
      - name: Deploy Bundle to Dev
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST_DEV }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN_DEV }}
          TF_PLUGIN_CACHE_DIR: ~/.terraform.d/plugin-cache
        run: databricks bundle deploy --target dev


  # ---------------- PROD DEPLOY ----------------
  deploy-prod:
    needs: deploy-dev
    runs-on: ubuntu-latest
    environment: prod

    steps:
      - uses: actions/checkout@v3

      - name: Install Databricks CLI (NEW)
        run: |
          curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
          databricks -v

      # Cache Terraform Provider
      - name: Cache Terraform Providers
        uses: actions/cache@v3
        with:
          path: ~/.terraform.d/plugin-cache
          key: terraform-${{ runner.os }}-databricks

      # Build wheel again for prod deployment
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Build Wheel
        run: |
          pip install --upgrade pip
          pip install wheel setuptools
          python setup.py bdist_wheel
          ls dist

      # Authenticate to PROD workspace
      - name: Configure Databricks Auth
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST_PROD }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN_PROD }}
        run: databricks current-user me

      # Deploy to PROD
      - name: Deploy Bundle to Prod
        env:
          DATABRICKS_HOST: ${{ secrets.DATABRICKS_HOST_PROD }}
          DATABRICKS_TOKEN: ${{ secrets.DATABRICKS_TOKEN_PROD }}
          TF_PLUGIN_CACHE_DIR: ~/.terraform.d/plugin-cache
        run: databricks bundle deploy --target prod