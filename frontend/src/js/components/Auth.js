import React from 'react'

export default class Login extends React.Component {
	
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="container">
				<div className="row align-items-center justify-content-center" style={{"height": "100vh"}}>
					<div className="col-4">
						<div className="card">
							<div className="card-header">Sign In to Freecome</div>
							<div className="card-block">
								<form action="">
									<div className="form-group">
										<label htmlFor="">Username</label>
										<input type="text" className="form-control" name="login"/>
									</div>
									<div className="form-group">
										<label htmlFor="">Password</label>
										<input type="password" className="form-control" name="password"/>
									</div>
									<button type="button" className="btn btn-success col-12">Sign in</button>
								</form>	
							</div>
							<div className="card-footer text-nowrap text-center">
								New to Freecome? <a href="">Create an account</a>.
							</div>
						</div>
					</div>
				</div>	
			</div>
		);
	}
}