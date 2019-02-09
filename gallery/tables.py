# gallery/tables.py
from django_tables2 import tables, TemplateColumn, Column
from .models import Image
from .models import Video
from .models import Audio


class ImageTable(tables.Table):
    details = TemplateColumn(template_name='gallery/button/view_details_image_column.html')   

    class Meta:
         model = Image
         fields = ('id','name', 'details')

         

class AudioTable(tables.Table):
    details = TemplateColumn(template_name='gallery/button/view_details_audio_column.html')   

    class Meta:
         model = Audio
         fields = ('id','name', 'details')



class VideoTable(tables.Table):

    details = TemplateColumn(template_name='gallery/button/view_details_video_column.html')   

    class Meta:
         model = Video
         fields = ('id','name', 'details')


        
