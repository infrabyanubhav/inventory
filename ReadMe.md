## Stockflow Inventory Case Study

This repository contains the implementation for the **Stockflow inventory management case study**. It is a small Django + Django REST Framework project that exposes APIs to manage companies, warehouses, products, inventory levels, suppliers, and product bundles, and to surface low‑stock alerts.

The original case study description is in this Google Doc (provided by the recruiter/assignment):  
`https://docs.google.com/document/d/18RsGFhkO6IImZhGgxdzh4TDM0MbvTz_q-gViKiilMN4/edit?usp=sharing`

### Tech stack
- **Backend**: Django 5 + Django REST Framework
- **Database**: SQLite (local dev)
- **Language**: Python 3.10+

### Project structure
- **`stockflow/stockflow`**: Django project settings, URLs, WSGI/ASGI.
- **`stockflow/inventory`**: Inventory app (models, serializers, views, URLs, tests).
- **`.github/workflows/ci.yml`**: GitHub Actions CI (install dependencies + run tests).

### Getting started
1. **Create and activate a virtualenv** (optional but recommended):
   - `python -m venv myenv`
   - `source myenv/bin/activate` (macOS/Linux) or `myenv\Scripts\activate` (Windows)
2. **Install dependencies**:
   - `pip install -r requirements.txt`
3. **Run migrations**:
   - `cd stockflow`
   - `python manage.py migrate`
4. **Run the dev server**:
   - `python manage.py runserver`
5. The API will be available at `http://127.0.0.1:8000/`.

### Key API endpoints (examples)
- **Low stock alerts**  
  - `GET /inventory/companies/<company_id>/alerts/low-stock`  
  - Returns low stock alerts for a given company.
- **Inventory CRUD** (example base)  
  - `GET /inventory/` – list inventory records  
  - `POST /inventory/` – create inventory record

> Note: The exact contract and business rules come from the case‑study document linked above; this implementation is aligned with that spec as closely as possible.

### Running tests
From the project root:
- `cd stockflow`
- `python manage.py test inventory`

GitHub Actions also runs these tests automatically on pushes/PRs to `main`.