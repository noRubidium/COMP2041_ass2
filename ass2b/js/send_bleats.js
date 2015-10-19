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
		return {value: value,length:value.length,longitude:"",latitude:"",data_uri:[]};
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
        var reader =[]; 
		var file = [];
		console.log(e.target.files.length);
        for(var i=0; i < e.target.files.length;i++){
        	file.push(e.target.files[i]);
			reader.push(new FileReader());
	        reader[i].onload = function(upload) {
				var li = this.state.data_uri;
				li.push(upload.target.result);
	            this.setState({
	                data_uri:li
	            });
	        }.bind(this);

	        reader[i].readAsDataURL(file[i]);
			console.log(this.state.data_uri);
        }
        
    },
	render: function() {
	  	var img=[];
		console.log("HI");
		console.log(this.state.data_uri.length);
		for(var i=0; i< this.state.data_uri.length;i++){
			console.log("HI");
			img.push(<div 
					className="col-xs-2">
					<img 
					src={this.state.data_uri[i]} 
					className="img-responsive"/>
				</div>);
		}
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
			<div 
				className="col-xs-12">
				<input 
					type="file" 
					accept="image/*" 
					name="myPic" 
					multiple="multiple"
					onChange={this.handleFile}/>
				{img}
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

