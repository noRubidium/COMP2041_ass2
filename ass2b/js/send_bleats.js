var divStyle = {
  borderRadius:0+"px" // 'ms' is the only lowercase vendor prefix
};	
var textStyle = {
	borderRadius:0+"px",
	marginBottom:20+"px",
};

var MarkdownEditor = React.createClass({
	getInitialState: function() {
		var value="";
		return {value: value,length:value.length,longitude:"",latitude:""};
	},
	handleChange: function() {
		var value = this.refs.textarea.value;
		if(value.length > 142){
			value=value.substr(0,142);
		}
		var length=value.length;
		this.setState({value: value,length:length});
	},
	getGeo: function (position){
		var lon=position.coords.longitude;
		var lat = position.coords.latitude;
		this.setState({longitude:lon,latitude:lat});
	},
	setLoc: function (){
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(this.getGeo);
		}
	},
	handleFile: function(e) {
        var reader = new FileReader();
        var file = e.target.files[0];

        reader.onload = function(upload) {
            this.setState({
                data_uri: upload.target.result
            });
            console.log(this.state.data_uri)
        }.bind(this);

        reader.readAsDataURL(file);
    },
	render: function() {
	  
		return (
		<div className="markdownEditor">
			<textarea 
				className="form-control" 
				ref="textarea"
				rows="3" name="bleat_content" 
				placeholder="What are you thinking right now?" 
				onChange={this.handleChange}
				value={this.state.value}
				style={textStyle}>{this.state.value}</textarea>
			<input 
				type="file" 
				accept="image/*" 
				name="myPic" 
				onChange={this.handleFile}/>
			<div 
				className="col-xs-2">
				<img 
				src={this.state.data_uri} 
				className="img-responsive"/>
			</div>
			<div 
				className="col-xs-5 col-md-3"
				>Get my location:
				<span 
					className="glyphicon glyphicon-map-marker" 
					onClick={this.setLoc} 
					></span>
			</div>
			<div 
				id="LocationSpace" 
				className="col-xs-3">
			</div>
			<input 
				name="longitude" 
				type="hidden" 
				id="longitude" 
				value={this.state.longitude}/>
			<input 
				name="latitude" 
				type="hidden" 
				id="latitude" 
				value={this.state.latitude}/>
			<div 
				className="col-xs-4">
				Charactors left: {142 - this.state.length}
			</div>
			<div className="col-xs-1">
				<input
					type="submit"
					className="btn" 
					name="action" 
					value="POST"
					style={divStyle}/>
			</div>
		</div>
		);
	}
});

ReactDOM.render(
	<MarkdownEditor />,
	document.getElementById('myDiv')
);

