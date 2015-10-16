var Register = React.createClass({
	getInitialState: function(){
		return {
			is_valid:false,
			valid_email:false,
			valid_username:false,
			valid_full_name:false,
			valid_password:false,
			valid_confirm_password:false,
			valid_file:true,
			valid_longitude:true,
			valid_latitude:true,
			valid_suburb:true,
			valid_intro:true
		};
	},
	reset_button: function(){
		this.setState(this.getInitialState());
	},
	validate:function(){
		//TODO
	},
	change_handle: function(){
		var email = this.refs.email.value;
		var re=/[\w\.]+\@([\w]+\.)+[A-Za-z0-9]{2,4}/;
		if(email.search(re) != -1){
			this.setState({valid_email:true});
		}else{
			this.setState({valid_email:false});
		}
		
		var username = this.refs.username.value;
		re=/[\w]{4,16}/;
		if(username.search(re) != -1){
			this.setState({valid_username:true});
		}else{
			this.setState({valid_username:false});
		}

		var full_name = this.refs.full_name.value;
		re=/[\w\s]+/;
		if(full_name.search(re) != -1){
			this.setState({valid_full_name:true});
		}else{
			this.setState({valid_full_name:false});
		}

		var password = this.refs.password.value;
		re=/[\w\-\s]{6,16}/;
		if(password.search(re) != -1){
			this.setState({valid_password:true});
		}else{
			this.setState({valid_password:false});
		}

		var confirm_password = this.refs.confirm_password.value;
		if(confirm_password == password ){
			this.setState({valid_confirm_password:true});
		}else{
			this.setState({valid_confirm_password:false});
		}

		var longitude = this.refs.longitude.value;
		re=/[\d]*[\.]?[\d]*/;
		if(longitude.search(re) != -1){
			this.setState({valid_longitude:true});
		}else{
			this.setState({valid_longitude:false});
		}
		var latitude = this.refs.latitude.value;
		re=/[\d]*[\.]?[\d]*/;
		if(latitude.search(re) != -1){
			this.setState({valid_latitude:true});
		}else{
			this.setState({valid_latitude:false});
		}
		var suburb = this.refs.suburb.value;
		re=/[\w\s]*/;
		if(suburb.search(re) != -1){
			this.setState({valid_suburb:true});
		}else{
			this.setState({valid_suburb:false});
		}
		if(confirm_password != password){
			this.setState({is_valid:false});
		}else{
			if(this.state.valid_email && this.state.valid_username && this.state.valid_full_name 
				&& this.state.valid_password && this.state.valid_file
				&& this.state.valid_longitude && this.state.valid_latitude 
				&& this.state.valid_suburb && this.state.valid_intro){
				this.setState({is_valid:true});
			}else{
				this.setState({is_valid:false});
			}
		}
	},
	render: function(){
		return (
				<form encType="multipart/form-data" action="register.cgi" method="post">
					<h2>Register</h2>
					<div className="col-xs-6">
						<div className="form-group">
							<label>Email address</label>
							<input type="email" name="email" className="form-control" onChange={this.change_handle} ref="email" placeholder="Email"/>
							<p className="help-block">Example: Andrew.t@cse.unsw.edu.au</p>
							{(
								this.state.valid_email
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>User name</label>
							<input type="text" name="username" className="form-control" onChange={this.change_handle} ref="username" placeholder="username"/>
							<p className="help-block">Can only include: A-Z, a-z, _, -, 0-9.</p>
							{(
								this.state.valid_username
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Full name</label>
							<input type="text" name="full_name" className="form-control" onChange={this.change_handle} ref="full_name" placeholder="full_name" />
							<p className="help-block">Can only include normal alphabets</p>
							{(
								this.state.valid_full_name
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Password</label>
							<input type="password" name="password" className="form-control" onChange={this.change_handle} ref="password" placeholder="Password"/>
							{(
								this.state.valid_password
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
							<p className="help-block">At least 8 digits, at most 16 digits</p>
						</div>
						<div className="form-group">
							<label>Confirm password</label>
							<input type="password" className="form-control" onChange={this.change_handle} ref="confirm_password" placeholder="" />
							{(
								this.state.valid_confirm_password
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
							<p className="help-block">Must be the same as the previous section</p>
						</div>
					</div>
					<div className="col-xs-6">
						<div className="form-group">
							<label>Upload your photo</label>
							<input type="file" name="file" onChange={this.change_handle} ref="picture_upload"  accept="image/*"/>
							{(
								this.state.valid_file
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Logitude</label>
							<input type="text" name="longitude" className="form-control" onChange={this.change_handle} ref="longitude" placeholder="longitude" />
							{(
								this.state.valid_longitude
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Latitude</label>
							<input type="text" name="latitude" className="form-control" onChange={this.change_handle} ref="latitude" placeholder="latitude"/>
							{(
								this.state.valid_latitude
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Suburb</label>
							<input type="text" name="suburb" className="form-control" onChange={this.change_handle} ref="suburb" placeholder="suburb" />
							{(
								this.state.valid_suburb
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
						<div className="form-group">
							<label>Self Introduction</label>
							<textarea name="self_intro" className="form-control" rows="3"/>
							{(
								this.state.valid_intro
								? <span className="glyphicon glyphicon-ok"/>
								: <span className="glyphicon glyphicon-remove"/>)}
						</div>
					</div>
					<div>This is {this.state.is_valid}</div>
					{(
						this.state.is_valid
						? <button type="submit" name="action" value="register" className="btn btn-default">Submit</button>
						: <button type="submit" className="btn btn-default" disabled>Submit</button>
					)}
					<button  className="btn btn-default" type="reset" onClick={this.reset_button}>Reset</button>
				</form>
	)}
});

var form = document.getElementById('register');

ReactDOM.render(
	<Register />,
	form
	);
