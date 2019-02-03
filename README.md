# SUTD Academic Scheduler

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

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

2. Create your `.env` environment file by making a duplicate of the `.env-example` and remove the `-example`. In the `.env` file, you can set environment related variables like your API_HOST or APP_ENV.

```
APP_ENV=local
API_HOST=http://localhost:9700/fake-api
```

3. Lastly, run the start command to get the project off the ground. This command will not only build your JS files using the Webpack `dev-server`, but it will also auto-compile your Stylus files on every `.styl` file save.

```
npm start
```

1. Head over to the host link to view the app!