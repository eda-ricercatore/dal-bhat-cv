#	To-Do List



Assumed knowledge and skills that are prerequisites for embedded machine/deep learning - good to know, but not necessarily required.
+ [numerical linear algebra](https://en.wikipedia.org/wiki/Numerical_linear_algebra)
	- [matrix decomposition](https://en.wikipedia.org/wiki/Matrix_decomposition)
		* singular-value decomposition (SVD)
		* LU decomposition
		* QR decomposition (or QR factorization)
	- [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
		* Gauss–Jordan elimination
+ [Vector calculus, or vector analysis](https://en.wikipedia.org/wiki/Vector_calculus)
+ [Ordinary differential equations, ODEs](https://en.wikipedia.org/wiki/Ordinary_differential_equation)
+ [partial differential equation, PDEs](https://en.wikipedia.org/wiki/Partial_differential_equation)
+ [multi-objective optimization](https://en.wikipedia.org/wiki/Multi-objective_optimization)
+ [design space exploration](https://en.wikipedia.org/wiki/Design_space_exploration)



To-do list:
+ learn how to implement a graph data structure using the adjacency map graph representation \cite[\S14.2, pp. 627; \S14.2.3, pp. 632]{Goodrich2013}.
	- Do so using object-oriented analysis and design (or object-oriented programming) in [*Python*](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/python.md)
+ Learn the basics of [object detection](https://en.wikipedia.org/wiki/Object_detection)
	- Know the difference between [training and inference](https://blogs.nvidia.com/blog/2016/08/22/difference-deep-learning-training-inference-ai/)
	- For object detection solutions based on neural networks, including artificial neural networks (ANNs) and deep learning algorithms, we should have a neural network for training, and an approximate version of the training neural network for inference.
	- That is, the inference neural network is an approximate model of the training neural network.
	- Partition the data set given to us into a internal training data set (2/3 of the given data set), and an internal test data set (1/3 of the given data set for inference).
+ Find a data set for an [object detection](https://en.wikipedia.org/wiki/Object_detection) problem in [computer vision](https://en.wikipedia.org/wiki/Computer_vision)
	- Implement an [end-to-end solution](https://www.techopedia.com/definition/19057/end-to-end-solution-e2es), or complete solution, for that object detection problem (e.g., detecting a cat, flower, or drone).
		* Create a [SQL database](https://en.wikipedia.org/wiki/SQL) to store records of image/video and its corresponding label.
			+ Each record in the database is a [2-tuple](https://en.wikipedia.org/wiki/Tuple).
			+ [A database is a set of records.](https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/databases_and_information_systems.md)
		* Read in each image/video from the data set as an input
		* Detect if the specific object (e.g., a cat, flower, or drone) is detected in the image/video
			+ Use TensorFlow and Keras to implement our convolutional/recurrent neural networks (CNN/RNN) for deep learning.
		* If specific object **is in** the image/video, return detected.
			+ Associate that particular image/video with the label "detected".
		* If specific object **is not in** the image/video, return "not detected".
			+ Associate that particular image/video with the label "not detected".
	- Important Note: You can probably find an implementation (or complete solution) for a number of object detection problems online.
	- This step helps you become familiar with the object detection problem.
+ Customize the end-to-end solution, or our object detection "flow," for drone detection.
	- This step helps you become familiar with the specific drone detection problem.
+ Approximate the training neural network to produce the inference neural network.
	- Use the [SqueezeNet](https://en.wikipedia.org/wiki/SqueezeNet) framework to sparsify the CNN/RNN (i.e., make the graph representation of the CNN/RNN more sparse), so that we can optimize for performance and get the CNN/RNN to fit into our chosen CUDA-based GPU platform.
+ Implement the inference neural network using C++17 and CUDA on the target GPU platform.
+ Iterate this process for different CNN/RNN architectures to perform multi-objective design space exploration of various choices/parameters, so that we can pick a suitable Pareto-optimal CNN/RNN architecture.



#	References

BibTeX entries for references that I used.

	@book{Goodrich2013,
		Address = {Hoboken, {NJ}},
		Author = {Goodrich, Michael T. and Tamassia, Roberto and Goldwasser, Michael H.},
		Publisher = {John Wiley {\rm \&}\ Sons},
		Title = {Data Structures and Algorithms in Python},
		Year = {2013}}











##	Notes about In-Text Citation

I use LaTeX and BibTeX notations \cite{Kopka2004} for in-text citations in this document.




#	Author Information

The MIT License (MIT)

Copyright (c) <2019> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
