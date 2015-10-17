var Bleat_replies = React.createClass({
  getInitialState: function() {
    return {
      bleats:[]
    };
  },

  componentDidMount: function() {
    $.get(this.props.source, function(result) {
      for(var lastGist in result){
        this.setState({
          bleats:this.state.bleats.push(lastGist)
        });
      }
    }.bind(this));
  },
  single_bleat: function(bleat){
    return (<div className="single_bleat">
      <!--This is for a single bleat displayed in preview form-->
      <div className="list-group" >
        <div className="list-group-item container">
          <div className="col-sm-12">{bleat.content}</div>
          <div className="col-sm-3">{bleat.author}</div>
          <div className="col-sm-4" align="right">
            <h6><small>{bleat.time}</small></h6>
          </div>
          <form  method="post" action="full_bleat.cgi">
          <div className="col-xs-1">
              <input type="hidden" name="bleat_No" value="{bleat.bleat_No}">
              <button className="btn delete_bleat" name="action" value="full_display">
                <span className="glyphicon glyphicon-zoom-in"></span>
              </button>
          </div>
          <div className="col-xs-1">
              <button className="btn delete_bleat" name="action" value="delete">
                <span className="glyphicon glyphicon-trash"></span>
              </button>
          </div>
          </form>
        </div>
      </div>
      <div className="list-group">
      </div>
    </div>);
},
  render: function() {
    l = [];
    return (

    );
  }
});

ReactDOM.render(
  <Bleat_replies source="https://api.github.com/users/octocat/gists" />,
  mountNode
);