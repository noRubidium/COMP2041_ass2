var RelevantBleats = React.createClass({
	getInitialState: function(){
		return {
			bleats:[]
		};
	},
	componentDidMount: function() {
		$.get(this.props.source, function(result) {
			for(var i=0; i < reult.length;i++ ){
				var lastReply = result[i];
				if (this.isMounted()) {
					this.setState({
						bleats: this.state.bleats.push(lastReply);
					});
				}
			}
			
		}.bind(this));
	},
	render: function() {
		return (
			<div />
		);
	}
});