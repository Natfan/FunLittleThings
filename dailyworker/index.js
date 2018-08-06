require('dotenv').config()

const http = require('http')
const octokit = require('@octokit/rest')()

const github = {
	email: process.env.GITHUB_EMAIL,
	owner: process.env.GITHUB_OWNER,
	token: process.env.GITHUB_TOKEN
}

dailyTasks()

async function dailyTasks() {
	const date = new Date()
	const delay = (((24 - date.getUTCHours()) * 60) - date.getUTCMinutes()) * 60000

	await updateTest()

	setTimeout(dailyTasks, delay)
	console.log(`${delay}ms until next update.`)
}

async function updateTest() {
	getRepoInfo('FunLittleThings')
}

/** API METHODS **/
async function getRepoInfo(repo) {
	try {
		await octokit.authenticate({
			type: 'oauth',
			token: github.token
		})

		const readme = await octokit.repos.getReadme({
			owner: github.owner,
			name: repo
		})
		//return await readme
	} catch (error) {
		console.error("There was an error. -> " + error)
		process.exit(1)
	}
}
