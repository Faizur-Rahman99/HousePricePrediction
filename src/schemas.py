from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
    MedInc: float = Field(
        ...,
        ge=0,
        le=20,
        description="Median income in tens of thousands of dollars.",
        examples=[8.3]
    )

    HouseAge: float = Field(
        ...,
        ge=1,
        le=100,
        description="Median house age in years.",
        examples=[25]
    )

    AveRooms: float = Field(
        ...,
        ge=1,
        le=20,
        description="Average number of rooms per household.",
        examples=[6.2]
    )

    AveBedrms: float = Field(
        ...,
        ge=0.1,
        le=10,
        description="Average number of bedrooms per household.",
        examples=[1.1]
    )

    Population: float = Field(
        ...,
        ge=1,
        le=50000,
        description="Population of the block.",
        examples=[1200]
    )

    AveOccup: float = Field(
        ...,
        ge=0.1,
        le=20,
        description="Average household occupancy.",
        examples=[3.2]
    )

    Latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="Latitude coordinate.",
        examples=[34.05]
    )

    Longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="Longitude coordinate.",
        examples=[-118.24]
    )