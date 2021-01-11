
## Before the session

* Clone this repo. `git clone git@github.com:david26694/tdd-session.git`
* You need to have `pytest` (version `6.0.1` ideally) installed.
* You need to be able to run the tests in this repo.


### Installation

To install from conda (you don't really need conda, but I recommend it):

```bash
conda create -y --name tdd-session python==3.7
conda install --force-reinstall -y -q --name tdd-session -c conda-forge --file requirements.txt
conda activate tdd-session
```

Check pytest version:

```bash
pytest --version
```

If you don't have conda available, you can always run
```bash
pip install pytest
```
and have `pytest` installed globally.

### Run tests

Run sample test:

```bash
pytest
```

Should return something like:

```bash
============================= test session starts ==============================
...

test/test_sample.py .                                                    [100%]

============================== 1 passed in 0.03s ===============================
```

## What is testing?

3 important concepts:
* Software testing: writing code that checks that your code works.
* Unit testing vs system testing. Example: Airbnb room booking. Steps: Visitor searches for room in given dates, chooses room, request email is sent to host, host accepts, send confirmation email to visitor.
    * System testing: simulate the whole process and check that it works.
    * Unit testing: test individual components.
        * When doing a search, only rooms available these dates appear.
        * When choosing a room, an email is sent to the host.
        * When host accepts a request, a confirmation email is sent.

![Unit vs system testing](https://github.com/david26694/tdd-session/blob/main/testing.png?raw=true)

* Test-driven development: write tests and after writing the tests, write your code.

Different use-cases:
* Big software systems - hard to keep track of all the codebase.
* Libraries: you want the code you deliver to work.
* Data science: mostly, data trasnformation steps. Data validation needs to be done often, but it is not technically unit testing.

## Why testing?

From [stackoverflow](https://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort):

* Unit Tests allows you to make big changes to code quickly. You know it works now because you've run the tests, when you make the changes you need to make, you need to get the tests working again.
* The tests and the code work together to achieve better code. Your code could be bad / buggy. Your TEST could be bad / buggy. Your are banking on the chances of both being bad / buggy being low. Often it's the test that needs fixing but that's still a good outcome.
* When faced with a large and daunting piece of work ahead writing the tests will get you moving quickly.
* Unit Tests help you really understand the design of the code you are working on. Instead of writing code to do something, you are starting by outlining all the conditions you are subjecting the code to and what outputs you'd expect from that.
* Unit Tests give you instant visual feedback, we all like the feeling of all those green lights when we've done. It's very satisfying. It's also much easier to pick up where you left off after an interruption because you can see where you got to - that next red light that needs fixing.

## Examples

* [calmcode](https://calmcode.io/pytest/introduction.html)
* [sktools](https://github.com/david26694/sktools/blob/master/tests/test_sktools.py)
* [sklego](https://github.com/koaning/scikit-lego/blob/master/tests/test_preprocessing/test_dictmapper.py)
* [DBT airflow](https://github.com/gocardless/airflow-dbt/blob/master/tests/operators/test_dbt_operator.py)

## In the session

We'll to develop the fizzbuzz function in a _test driven development_ style. The fizzbuzz function does the following:

> Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
