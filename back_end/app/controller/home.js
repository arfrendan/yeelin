'use strict';

const Controller = require('egg').Controller;

class HomeController extends Controller {
  async index() {
    const { ctx } = this;
    ctx.body = '小林请我吃饭';
  }
}

module.exports = HomeController;
