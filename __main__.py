import skvideo.io
from matplotlib import pyplot as plt
import random
import os
import twitter

# Return 'num_images' no. of random images


def random_items(iterator, num_images=1):
    selected_items = [None] * num_images

    for item_index, item in enumerate(iterator):
        for selected_item_index in xrange(num_images):
            if not random.randint(0, item_index):
                selected_items[selected_item_index] = item

    return selected_items

# Read the video, extract images and save them to a directory


def extract_images(video_path, num_images, save_to_path):
    # Use vreader as it loads the video frame-by-frame
    # If it is a large video, using vread() may exhaust the memory
    if not os.path.exists(save_to_path):
        os.makedirs(save_to_path)

    videogen = skvideo.io.vreader(video_path)
    random_set = random_items(videogen, num_images)

    count = 0

    for frame in random_set:
        directory = "{0}/image{1}.png".format(save_to_path, count)
        plt.imsave(directory, frame)
        # if you instead want to just show the images in a notebook
        # instead of saving, use imshow()
        # plt.imshow(frame, interpolation='nearest')
        plt.show()
        count += 1


if __name__ == '__main__':
    api = twitter.Api(consumer_key="yelpVEHNFclN2fv2pk6CFnFRn",
                      consumer_secret="FA55R7x6afgr4unWYGMBJ2CJsVQx05XwfTiRDCopSFlZg0e6XD",
                      access_token_key="1000107957940518912-QBWvKmpovcpDf2lRk5GcSeQhIn77NK",
                      access_token_secret="Z7E0w9xUkKhf3sZOZl22Lr7YC2h5RDYMp0hIL8PbYldr2")

    status = api.PostUpdate('I love python-twitter!',
                            media='/home/victor/Pictures/image0.png')
    print(status.text)

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--video-path', required=True)
# parser.add_argument('--num-images', required=True)
# parser.add_argument('--save-to-path', required=True)
# args = parser.parse_args()

    video_path = "/home/victor/Videos/thiago.mp4"
    num_images = 1
    save_to_path = "/home/victor/Pictures"

    # extract_images(args.video_path, int(args.num_images), args.save_to_path)
    extract_images(video_path, num_images, save_to_path)
