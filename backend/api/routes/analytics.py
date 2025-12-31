from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user
from analytics.python.student_analysis import get_student_report
from analytics.python.class_analysis import get_class_average

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/student/{student_id}")
def student_analytics(student_id: int, user=Depends(get_current_user)):
    return get_student_report(student_id)

@router.get("/class/{class_name}")
def class_analytics(class_name: str, user=Depends(get_current_user)):
    return get_class_average(class_name)
