# Django Project Template [![Build Status](https://secure.travis-ci.org/sfchronicle/django-project-template.png?branch=master)](http://travis-ci.org/sfchronicle/django-project-template) [![GitHub version](https://badge.fury.io/gh/sfchronicle%2Fdjango-project-template.svg)](http://badge.fury.io/gh/sfchronicle%2Fdjango-project-template)

Django Project Template is a collection of development tasks and optimizations aimed at anyone doing news application development on tight deadlines in Django. Highlights include:

- Works with CIR's custom built [Yeoman generator](https://github.com/cirlabs/generator-newsapp) for even faster front-end scaffolding, development and optimization with [Grunt](http://gruntjs.com/) and [Bower](http://bower.io/) (__recommended__)
- [PostGIS](http://postgis.net/) setup for geospatial database work
- [Fabric](http://www.fabfile.org/) tasks for development, building and deployment
- Preconfigured with [Django Compressor](http://django-compressor.readthedocs.org/en/latest/) for CSS and JS preprocessing, concatenation and minification
- Preconfigured deploy chain for baking projects flat with [Django Bakery](http://django-bakery.readthedocs.org/en/latest/)
- [AWS CLI](https://aws.amazon.com/cli/) for easy deployment to [Amazon S3](https://aws.amazon.com/s3/)
- `lib` directory with some of our favorite code snippets and custom Django mangement commands

## Minimum Requirements
This project supports Ubuntu Linux 14.04 and Mac OS X Yosemite. It is not tested or supported for the Windows OS.

- [Django 1.8+](https://www.djangoproject.com/)
- [PostgreSQL 9.3+](http://www.postgresql.org/)
- [PostGIS 2.1+](http://postgis.net/)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
- (optional) [Node.js 0.12.x](http://nodejs.org/) or [io.js 1.2.x](https://iojs.org/en/index.html)

## Quickstart
```bash
$ mkvirtualenv project_name
$ pip install django fabric
$ django-admin.py startproject --extension=py,.gitignore --template=https://github.com/sfchronicle/django-project-template/archive/master.zip project_name
$ cd project_name
$ fab bootstrap # bootstrap project
```

### Using Yeoman, Grunt and Bower (__recommended__)
While this template works fine out the box, it's recommended you use use our yeoman generator to manage your static assets (HTML, CSS, JS). We built [generator-newsapp](https://github.com/sfchronicle/generator-newsapp) to work in concert with this project template. For this to work you'll need [Node.js 0.12.x](http://nodejs.org/)

After running the quick start above run `fab scaffold` to install the required node.js libraries and generate the templates needed for frontend development.

**Note**: If you already have the npm modules installed, you can skip installing them by running `fab scaffold:skip-install`.

## Deployment
This project assumes you have an Amazon S3 bucket where you host your apps. They are static apps with no database calls.

Update `settings/production.py` with the various s3 buckets you'll use. We have buckets for staging (testing the application), buckets for media assets and a final bucket publishing. You can use these conventions or change them. You'll also need to add the [Django Bakery views](http://django-bakery.readthedocs.org/en/latest/gettingstarted.html#configuration) you want generated.

### Configure AWS cli
We use the AWS command-line interface to publish the Django Bakery created project to Amazon S3. If you haven't [sign up for Amazon Web Services and get your access key id and secret access key](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html).

After setting up AWS, install the AWS command-line interface globally. For example:

```bash
$ sudo pip install awscli
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE  # this is fake, never share this!!
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  # this is fake
Default region name [None]: us-west-1
Default output format [None]: ENTER
```
For more, read the [AWS Command Line Interface Getting Started Guide](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

Now, run `fab publish` to publish your application to the world.

### PostGIS
By default, this project assumes you'll be using PostGIS as your database. If you'd prefer not to, you can set the `USE_POSTGIS` variable in `settings/common.py` to `False` and the project will default to PostgreSQL. :warning: Be sure to do this BEFORE running the quickstart.

### Tasks
Here are the various fabric tasks included in the project. See [fabfile.org](http://fabfile.org) to learn more about Fabric and Python task execution.

```
bootstrap       Run commands to setup a new project
bower           Alias to run bower within Django project
clear           Remove a model from an application database
compress        shortcut for Django compressor offline compression command
createdb        Creates local database for project
s3deploy        Deploy project to S3.
destroy         destroys the database and Django project. Be careful!
dropdb          drops local database for project
grunt_build     Execute grunt build task
npm             Alias to run npm within Django project
publish         Compress, build and deploy project to Amazon S3.
reset           delete all the deploy code
rs              Start development server and grunt tasks. Optionally, specify port
scaffold        Setup front-end management for Django project with yo, grunt and bower.
sh              Run Django extensions shell
startapp        Create Django app
unbuild         shortcut for Django bakery unbuild command
```

### Help
Need help? Open an issue in: [ISSUES](https://github.com/sfchronicle/django-project-template/issues)

### Contributing
Want to improve the template? Fork the repo, add your changes and send a pull request.

### License
The MIT License (MIT)

Copyright (c) '93 Til ... The San Francisco Chronicle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
