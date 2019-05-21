#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to partition
		a data set into the following ratios for the following
		purposes.
	# 2:1:1 (50%, 25%, 25%) for training, validation, and testing
		in machine learning.
	# 2:1 (67%, 33%) for training and cross validation.



	#### IMPORTANT NOTES:
	[Insert references for why the aforementioned ratios were
		chosen for YOLO, one-shot detection, and similar
		machine learning techniques]


	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).



#### TO BE COMPLETED

"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?



###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
				To make system calls.
	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.
	filecmp		For file comparison.
	calendar	For calendar-related functions.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import calendar
# Note included in the above menu yet.
from os import listdir
from os.path import isfile, isdir, join
from os import walk
from collections import Counter
import string



###############################################################
#	Import Custom Python Modules



###############################################################
"""
	Module that partitions the data set for either of the
		following in machine learning:
		1) training, validation, and testing; or,
		2) training and cross validation.
"""
class partition_data_set:
	# =========================================================
	##	Method to partition data set into 2:1:1 (50%, 25%, 25%)
	#		for training, validation, and testing.
	#	@return - List of names for sets of video frames, or
	#		names of subfolders in the data set.
	#	O(n) method, where n is the number of "videos" in the
	#		data set.
	@staticmethod
	def partition_2_1_1(dict_of_labels_and_instances):
		print("=	Partition into 2:1:1 (50%, 25%, 25%).")
	# =========================================================
	##	Method to partition data set into 2:1 (67%, 33%) for
	#		training and cross validation.
	#	@return - List of names for sets of video frames, or
	#		names of subfolders in the data set.
	#	O(n) method, where n is the number of "videos" in the
	#		data set.
	@staticmethod
	def partition_2_1():
		print("=	Partition into 2:1 (67%, 33%).")
	# =========================================================
	##	Method to obtain the names of the subdirectories.
	#		Solution #1.
	#	Each subdirectory/subfolder is a set of video frames
	#		from a video of an object that we have to detect.
	#	@return - List of names for sets of video frames, or
	#		names of subdirectories in the data set.
	#	O(n) method, where n is the number of "videos" in the
	#		data set.
	@staticmethod
	def get_names_of_subdirectories1(location_of_data_set):
		print("=	Get names of subdirectories: Method #1.")
		if os.path.isdir(location_of_data_set):
			# Get the names of the subdirectories.
			onlydirs = [f for f in listdir(location_of_data_set) if isdir(join(location_of_data_set, f))]
			onlydirs = sorted(onlydirs, key=str.lower)
			print("onlydirs",onlydirs,"=")
			return onlydirs
		else:
			"""
				location_of_data_set is not a directory

				Future work: Change "return []" to raising
					an user-defined error.
			"""
			return []
	# =========================================================
	##	Method to obtain the names of the subdirectories.
	#		Solution #2.
	#	Each subdirectory/subfolder is a set of video frames
	#		from a video of an object that we have to detect.
	#	@return - List of names for sets of video frames, or
	#		names of subdirectories in the data set.
	#	O(n) method, where n is the number of "videos" in the
	#		data set.
	@staticmethod
	def get_names_of_subdirectories2(location_of_data_set):
		#print("=	Get names of subdirectories: Method #2.")
		if os.path.isdir(location_of_data_set):
			# Get the names of the subdirectories.
			f = []
			for (dirpath, dirnames, filenames) in walk(location_of_data_set):
				#f.extend(filenames)
				f.extend(dirnames)
				break
			dirnames = sorted(dirnames, key=str.lower)
			#print("dirnames",dirnames,"=")
			return dirnames
		else:
			"""
				location_of_data_set is not a directory

				Future work: Change "return []" to raising
					an user-defined error.
			"""
			return []
	# =========================================================
	##	Method to count the number of video per category (or
	#		class - in terms of classification in pattern
	#		recognition).
	#	From a list of video names, determine the number of
	#		instances of each video category.
	#	@return - Dictionary of (category, number of instances
	#		of each video category).
	#	O(n) method, where n is the number of "videos" in the
	#		data set.
	@staticmethod
	def count_number_of_videos_per_category(list_of_video_names):
		list_of_categories = []
		for i in list_of_video_names:
			list_of_categories.append(i.rstrip(string.digits))
		print("list_of_categories",list_of_categories,"=")
		dict_of_categories_and_number_of_instances = Counter(list_of_categories)
		print("dict_of_categories_and_number_of_instances",dict_of_categories_and_number_of_instances,"=")
		return dict_of_categories_and_number_of_instances




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	"""
		Variables used to parameterize our solution.
	"""
	directory_of_data_set = "../../dac-2019-sdc"
	#list_of_subdirectories = partition_data_set.get_names_of_subdirectories1(directory_of_data_set)
	list_of_subdirectories = partition_data_set.get_names_of_subdirectories2(directory_of_data_set)
	dict_of_categories_and_instances = partition_data_set.count_number_of_videos_per_category(list_of_subdirectories)
	partition_data_set.partition_2_1_1(dict_of_categories_and_instances)
	partition_data_set.partition_2_1(dict_of_categories_and_instances)
