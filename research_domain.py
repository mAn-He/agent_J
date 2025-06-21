# research_domain.py

from enum import Enum

class ResearchDomain(Enum):
    """
    Specifies the various research domains that the system can classify.
    연구 시스템이 분류할 수 있는 다양한 연구 분야를 정의합니다.
    """
    MATERIALS_SCIENCE = "materials_science"
    BIOENGINEERING = "bioengineering"
    MECHANICAL_ENGINEERING = "mechanical_engineering"
    ELECTRICAL_ENGINEERING = "electrical_engineering"
    CHEMICAL_ENGINEERING = "chemical_engineering"
    COMPUTER_SCIENCE = "computer_science"
    PHYSICS = "physics"
    CHEMISTRY = "chemistry"
    ENVIRONMENTAL_SCIENCE = "environmental_science"
    FORESTRY = "forestry"
    AGRICULTURE = "agriculture"
    HEALTHCARE = "healthcare"
    FINANCE = "finance"
