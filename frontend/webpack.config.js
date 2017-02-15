const path = require('path');
const webpack = require('webpack');

module.exports = {
    devtool: 'source-map',
    entry: {
        index: ['./src/js/app.js']
    },
    output: {
        path: path.join(__dirname, 'public/js/'),
        filename: '[name].js',
    },
    module: {
        loaders: [{
            test: /\.js?/,
            loader: 'babel-loader',
            exclude: /node_modules/,
            query: {
                presets: ['es2015', 'react'],
                plugins: ['transform-decorators-legacy'],
            }
        }, {
            test: /\.css$/,
            loader: "style-loader!css-loader"
        }]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin()
    ],
    devServer: {
        contentBase: path.join(__dirname, "public"),
        host: 'localhost',
        port: 3310,
        hot: true,
        historyApiFallback: true
    }
};