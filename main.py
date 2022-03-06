# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import list_cams
import vlc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import ffmpeg_streaming
    from ffmpeg_streaming import Formats, Bitrate, Representation, Size

    capture = ffmpeg_streaming.input('0', capture=True)

    print_hi('PyCharm')
    list_cams.list_ports()
    import vlc





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
