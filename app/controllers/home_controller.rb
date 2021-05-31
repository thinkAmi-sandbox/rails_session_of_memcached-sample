class HomeController < ApplicationController
  def index
    session[:foo] = 'bar'
  end

  def reset
    reset_session
  end
end
