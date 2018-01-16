# missing_frame
print the frame range of an animated seq listing out available frames. This will help detect missing frames.



		
## Description:

to check if there are any missing frame in the rendered out animated sequence where each render out frame is name in this particular pattern

		name.####.ext
		eg: smoke.1001.exr

result :
		[1001-1005, 1009-1027 and so on] 


## Getting Started

the program take an input from the user to be entered in the terminal:
"path of the seq folder"

based on this input it iterates through the files in the given input folder.


