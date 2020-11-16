from setuptools import setup

setup(
    name="IotLibrary",
    version="1.0",
    install_requires=[
        "requests",
        "bcrypt",
		"six",
		"txthings",
		"twisted",
		"coapthon",
		"aiocoap",
		"asyncio",
		"docutils pygments pypiwin32 kivy_deps.sdl2==0.1.22 kivy_deps.glew==0.1.12",
		"kivy_deps.angle==0.1.9",
		"kivy==1.11.1",
		"kivy_examples==1.11.1",
		"kivy_deps.gstreamer==0.1.17",
		"Arduino-Python3pip3 ",
		"cbor",
		"LinkHeader",
    ],
    # ...
)