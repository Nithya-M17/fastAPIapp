from fastapi import APIRouter, HTTPException, status
from schemas.job import JobCreate, JobUpdate

router = APIRouter(
    prefix="/job",
    tags=["job"]
)

jobs = []


# Create Job
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate):
    jobs.append(job)
    return job


# Get All Jobs
@router.get("/", status_code=status.HTTP_200_OK)
def get_all_job():
    return jobs


# Get Job by ID
@router.get("/{job_id}", status_code=status.HTTP_200_OK)
def get_job(job_id: int):
    if job_id >= len(jobs):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    return jobs[job_id]


# Update Job
@router.put("/{job_id}", status_code=status.HTTP_200_OK)
def update_job(job_id: int, job: JobUpdate):
    if job_id >= len(jobs):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    jobs[job_id] = job
    return jobs[job_id]


# Delete Job
@router.delete("/{job_id}", status_code=status.HTTP_200_OK)
def delete_job(job_id: int):
    if job_id >= len(jobs):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    deleted_job = jobs.pop(job_id)

    return {
        "message": "Job deleted successfully",
        "job": deleted_job
    }