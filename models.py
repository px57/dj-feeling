from django.forms import model_to_dict
from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel

class Feeling(BaseMetadataModel):
    """
        @description: 
    """
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='feelings',
        null=True,
        blank=True  
    )

    like_or_dislike = models.IntegerField(
        default=-1,
        choices=(
            (-1, 'none'),
            (0, 'dislike'),
            (1, 'like')
        )
    )

    reasons = models.TextField(
        null=True,
        blank=True
    )

    # -> Get the model object
    relatedModel = models.CharField(
        max_length=255, 
        null=True, 
        blank=True
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True, 
        blank=True
    )

    def __str__(self):
        """
            @description: 
        """
    
    def serialize(self, request):
        """
            @description:
        """
        serialized = model_to_dict(self)
        return serialized
    
    