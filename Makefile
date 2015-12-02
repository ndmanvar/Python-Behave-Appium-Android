run_all_in_parallel:
	make -j android_emulator samsung_galaxy_s4_emulator

android_emulator:
	deviceName="Samsung Galaxy S5 Device" behave-parallel/bin/behave --processes 12 --parallel-element scenario

samsung_galaxy_s4_emulator:
	deviceName="Samsung Galaxy S4 Device" behave-parallel/bin/behave --processes 12 --parallel-element scenario
