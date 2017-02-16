import React from 'react'

export default (props) =>
{
	return(
		<form action="">
			<div className="form-group">
				<label htmlFor="">Description:</label>
				<input type="text" className="form-control"/>
			</div>
			<div className="form-group">
				<label htmlFor="">Category:</label>
				<select className="custom-select col-12" name="" id="">
					<option value="">Salary</option>
					<option value="">Business</option>
					<option value="">Dividens</option>
					<option value="">Gifts</option>
					<option value="">Extra work</option>
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
	)
}