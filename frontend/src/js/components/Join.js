import React from 'react'

export default class Join extends React.Component {
	
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="container">
				<div className="row align-items-center justify-content-center" style={{"height": "100vh"}}>
					<div className="col-4">
						<div className="card">
							<h5 className="card-header">Join to Freecome</h5>
							<div className="card-block">
								<form action="">
									<div className="form-group">
										<label htmlFor="">Username</label>
										<input type="text" className="form-control" name="login"/>
										<small className="form-text text-muted">Username will be used for a access.</small>
									</div>
									<div className="form-group">
										<label htmlFor="">Email Address</label>
										<input type="email" className="form-control" name="email"/>
										<small className="form-text text-muted">We will never share your email with anyone else.</small>
									</div>
									<div className="form-group">
										<label htmlFor="">Password</label>
										<input type="password" className="form-control" name="password"/>
										<small className="form-text text-muted">At least five characters.</small>
									</div>
									<button type="button" className="btn btn-success col-12">Create an account</button>
								</form>	
							</div>
							<div className="card-footer text-nowrap text-center">
								Already have an account? <a href="/login">Sign in</a>.
							</div>
						</div>
					</div>
				</div>	
			</div>
		);
	}
}