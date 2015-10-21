	var mountNode = document.getElementById('notification')
	var UserGist = React.createClass({
	  getInitialState: function() {
	    return {
	      username: '',
	      lastGistUrl: ''
	    };
	  },

	  componentDidMount: function() {
	    $.get(this.props.source, function(result) {
	    	console.log(result);
	      var lastGist = result;
		console.log(lastGist);
	      if (this.isMounted()) {
		this.setState({
		  username: lastGist.username,
		  lastGistUrl: lastGist.listens
		});
	      }
	    }.bind(this));
	  },
	  componentDidUpdate: function() {
	    $.get(this.props.source, function(result) {
	      console.log(result);
	      var lastGist = result;
	  console.log(lastGist);
	      if (this.isMounted()) {
		this.setState({
		  username: lastGist.username,
		  lastGistUrl: lastGist.listens
		});
	      }
	    }.bind(this));
	  },
	  render: function() {
	    return (
	      <div>
		{this.state.username}'s last gist is
		<a >{this.state.lastGistUrl} here</a>.
	      </div>
	    );
	  }
	});
