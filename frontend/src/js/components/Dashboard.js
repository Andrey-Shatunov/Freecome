import React from 'react'

export default class Dashboard extends React.Component {
	
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="container">
				<div className="row align-items-center" style={{"height": "100vh"}}>
					<div className="col">
						<div className="card">
							<h5 className="card-header">Expenditures</h5>
							<div className="card-block">
								<form action="">
									<div className="form-group">
										<label htmlFor="">Description:</label>
										<input type="text" className="form-control"/>
									</div>
									<div className="form-group">
										<label htmlFor="">Category:</label>
										<select className="custom-select col-12" name="" id="">
											<option value="">Food</option>
											<option value="">Lunch</option>
											<option value="">Fuel</option>
											<option value="">Gifts</option>
											<option value="">Hosting</option>
										</select>
									</div>
									<div className="form-group">
										<label htmlFor="">Amount:</label>
										<div className="input-group">
											<input type="number" className="form-control" id="income" name="income" placeholder="1000"/>
											<div className="input-group-addon">₽</div>	
										</div>	
									</div>
									<button className="btn btn-primary" style={{"width": "100%"}}>Add</button>
								</form>
							</div>
							<div className="card-block">
								<table className="table table-hover">
									<thead>
										<tr>
											<td>Description</td>
											<td>Amount</td>
											<td></td>
											<td></td>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>Food</td>
											<td>1200₽</td>
											<td></td>
											<td>
												<button type="button" className="close" aria-label="Close">
												  <span aria-hidden="true">&times;</span>
												</button>
											</td>
										</tr>
									</tbody>
								</table>	
							</div>
						</div>
					</div>
				</div>
			</div>	
		)
	}
}