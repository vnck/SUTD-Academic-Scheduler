# SUTD Academic Scheduler

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

To run:
Clone the repository.

Make sure to have Node JS installed (see below).

Navigate to `/flask-scheduling server` and run the command
```
python models.py
python flaskApp.py
```

Navigate to `/react-app` and run the command
```
npm install 
npm start
```

View app on <http://localhost:3000/login>

## Requirements

For development, you will only need Node.js installed on your environement.
Please use the appropriate [Editorconfig](http://editorconfig.org/) plugin for your Editor (not mandatory).

### Node

[Node](http://nodejs.org/) is really easy to install & now include [NPM](https://npmjs.org/).
You should be able to run the following command after the installation procedure
below.

    $ node --version
    v0.10.24

    $ npm --version
    1.3.21

#### Node installation on OS X

You will need to use a Terminal. On OS X, you can find the default terminal in
`/Applications/Utilities/Terminal.app`.

Please install [Homebrew](http://brew.sh/) if it's not already done with the following command.

    $ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

If everything when fine, you should run

    brew install node

#### Node installation on Linux

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs

#### Node installation on Windows

Just go on [official Node.js website](http://nodejs.org/) & grab the installer.
Also, be sure to have `git` available in your PATH, `npm` might need it.

---

## Getting Started
In order to get started developing, you'll need to do a few things first.

1. Install all of the `node_modules` required for the package. Depending on your computer's configuration, you may need to prefix this command with a `sudo`.
```
npm install
```
or
```
sudo npm install
```

2. Run the start command to get the project off the ground. This command will not only build your JS files using the Webpack `dev-server`, but it will also auto-compile your Stylus files on every `.styl` file save.

```
npm start
```

1. Head over to the host link to view the app!
