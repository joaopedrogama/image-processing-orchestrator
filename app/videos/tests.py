from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ninja_extra.testing import TestClient
from videos.models import Video
from videos.controllers import VideoController

class VideoControllerTest(TestCase):

    def setUp(self):
        self.client = TestClient(VideoController)
        self.test_video = SimpleUploadedFile(
            "test_video.mp4", b"file_content", content_type="video/mp4"
        )

    def test_create_video(self):
        form_data = {
            "name": "Test Video",
        }

        response = self.client.post(
            "/",
            data=form_data,
            FILES={"video_file": self.test_video},
            format="multipart",
        )

        self.assertEqual(response.status_code, 200)

        video = Video.objects.first()

        self.assertEqual(video.name, "Test Video")
        self.assertRegex(video.video_file.name, r"^videos/test_video.*\.mp4$")


    def test_list_videos(self):
        Video.objects.create(name="Video 1", video_file="video1.mp4")
        Video.objects.create(name="Video 2", video_file="video2.mp4")

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)
