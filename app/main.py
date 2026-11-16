from fastapi import FastAPI, HTTPException
from app.database import init_db, get_db_connection
from app.models import WorkOrderCreate, WorkOrderResponse

app = FastAPI(
    title="Supply Chain & Maintenance Readiness Copilot",
    description="AI-assisted maintenance triage and parts readiness API",
    version="0.1.0"
)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "0.1.0"}

@app.get("/inventory/{part_id}")
def get_part_stock(part_id: str):
    conn = get_db_connection()
    part = conn.execute("SELECT * FROM inventory WHERE part_id = ?", (part_id.upper(),)).fetchone()
    conn.close()
    if not part:
        raise HTTPException(status_code=404, detail=f"Part {part_id} not found")
    return dict(part)

@app.post("/work-orders", response_model=WorkOrderResponse)
def create_work_order(order: WorkOrderCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO work_orders (equipment_id, fault_code, issue_description) VALUES (?, ?, ?)",
        (order.equipment_id, order.fault_code, order.issue_description)
    )
    order_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {**order.model_dump(), "id": order_id, "status": "OPEN"}
