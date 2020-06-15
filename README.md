# bayesian_gym
Collection of courses, examples, notebooks to train many important modern applications of Bayesian filtering such as state estimation, sensor fusion, linear and nonlinear filtering, single and multi-object tracking and more.

# Sources
The following precisely describes the sequence of courses and lectures i followed. In the end attempt to souggest an ideal path that weighs all pros and cons of individual courses and gives the most optimal gains for dedicated time.

1) edX course - [Sensor Fusion and Non-linear Filtering for Automotive Systems](https://courses.edx.org/courses/course-v1:ChalmersX+ChM015x+2T2020/course/).
__Time:__ Took 5 days, averaging 4 hours every day 
__Pros:__ Free. Really good theoretical background for Bayesian filtering and detailed mathematical derrivation of linear, extended, uncented and cubature Kalman filters together with particle filters. The course asks you do complete a few exercises after each lecture to deepen the new knowledge.
__Cons:__ Most useful project-like exercises, for example MATLAB coding of filters is hidden behind approx 300 USD paycheck. 

2) Python library for Kalman and Particle filter - [filterpy](https://filterpy.readthedocs.io/en/latest/#id6) and [the companion book](https://nbviewer.jupyter.org/github/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/table_of_contents.ipynb)
__Time:__ Took around 10 days 6-8 hours a day
__Pros:__ Companion book nicely builds explanations of Kalman filters from ground up. Self contained does not require any background knowledge on the topic, all necessary mathematics is presented. Author goes for an thorough but intuitive explanations before most of the math is presented. Jupyter notebook allows to create interactive examples where user is in control of the input and can study the consequences which add up to learning experience. Author also gives good examples not only for the application of filterpy but also design of Kalman filter for different cases.
__Cons:__ haven't found any, beginner book totally worth every sencond spent

3) edX course [Multi-Object Tracking for Autonomous Systems](https://courses.edx.org/courses/course-v1:ChalmersX+ChM013x+1T2020/course/)
__Time__: SOT part 2 weeks,
__Pros__: Very detailed, this time coding assignments are not locked behind the payceck
__Cons__: Although being an awesome intro to object tracking, reqires very solid background builds on top sensor fusion course and additional knowledge statistics.

# TODO
0) Create Pipenv
1) Add interesting datasets fx single object tracking from Malthes thesis, bugs for MOT, and more. The more different the etter
2)


