from feeling.models import Feeling

def load_or_create_feel(
    relatedModel: str, 
    relatedModelId: int,
    profile: object or None):
    """
        @description: 
    """
    dbFeeling = Feeling.objects.filter(
        relatedModel=relatedModel,
        relatedModelId=relatedModelId,
        profile=profile
    ).first()

    if dbFeeling is None:
        dbFeeling = Feeling(
            relatedModel=relatedModel,
            relatedModelId=relatedModelId,
            profile=profile
        )
        dbFeeling.save()

    return dbFeeling