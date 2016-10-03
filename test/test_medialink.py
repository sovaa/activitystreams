from activitystreams.models.medialink import MediaLink
from activitystreams.models.tags import Tags
from activitystreams.exception import ActivityException

import unittest


class MediaLinkTest(unittest.TestCase):
    def test_duration(self):
        link = MediaLink({Tags.DURATION: '2'})
        self.assertEqual(link.duration, 2)

    def test_width(self):
        link = MediaLink({Tags.WIDTH: '1024'})
        self.assertEqual(link.width, 1024)

    def test_height(self):
        link = MediaLink({Tags.HEIGHT: '768'})
        self.assertEqual(link.height, 768)

    def test_duration_empty_ok(self):
        link = MediaLink({Tags.DURATION: '  '})
        self.assertEqual(link.duration, None)

    def test_width_empty_ok(self):
        link = MediaLink({Tags.WIDTH: '  '})
        self.assertEqual(link.width, None)

    def test_height_empty_ok(self):
        link = MediaLink({Tags.HEIGHT: '  '})
        self.assertEqual(link.height, None)

    def test_url_empty_ok(self):
        link = MediaLink({Tags.URL: '   '})
        self.assertEqual(link.height, None)

    def test_invalid_duration(self):
        self.assertRaises(ActivityException, MediaLink, {Tags.DURATION: 'asdf'})

    def test_invalid_width(self):
        self.assertRaises(ActivityException, MediaLink, {Tags.WIDTH: 'asdf'})

    def test_invalid_height(self):
        self.assertRaises(ActivityException, MediaLink, {Tags.HEIGHT: 'asdf'})

    def test_empty(self):
        MediaLink({})

    def test_none(self):
        MediaLink(None)

    def test_url_invalid_ok(self):
        link = MediaLink({Tags.URL: 'asdf'})
        self.assertEqual(link.url, 'asdf')

    def test_url(self):
        link = MediaLink({Tags.URL: 'http://google.com/'})
        self.assertEqual(link.url, 'http://google.com/')
