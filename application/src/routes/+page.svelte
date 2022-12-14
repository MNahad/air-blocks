<script lang="ts">
	import '@material/web/button/elevated-button.js';
	import '@material/web/textfield/filled-text-field.js';
	import { Gateway, Wallet, type WalletStore } from 'fabric-network';

	class OpfsWallet implements WalletStore {
		private root;
		private walletHandle;
		constructor() {
			this.root = navigator.storage.getDirectory();
			this.walletHandle = this.root.then((root) => root.getDirectoryHandle('wallet'));
		}
		async get(label: string): Promise<Buffer | undefined> {
			const fileHandle = await (await this.walletHandle).getFileHandle(label);
			return Buffer.from(await (await fileHandle.getFile()).text());
		}
		async list(): Promise<string[]> {
			const files = [];
			for await (const handle of (await this.walletHandle).values()) {
				files.push(handle.name);
			}
			return files;
		}
		async put(label: string, data: Buffer): Promise<void> {
			await this.remove(label);
			const fileHandle = await (await this.walletHandle).getFileHandle(label, { create: true });
			const writable = fileHandle.createWritable();
			await writable.write(data.buffer);
			await writable.close();
		}
		async remove(label: string): Promise<void> {
			await (await this.walletHandle).removeEntry(label);
		}
	}
	class AuthRepository {
		async getConnectionProfile(): Promise<Record<string, unknown>> {
			const dirHandle = await navigator.storage.getDirectory();
			const file = await dirHandle.getFileHandle('connection_profile');
			return JSON.parse(await (await file.getFile()).text());
		}
		async getWallet(): Promise<Wallet> {
			return new Wallet(new OpfsWallet());
		}
		async getUserId(): Promise<string> {
			const dirHandle = await navigator.storage.getDirectory();
			const user = await dirHandle.getFileHandle('user');
			return (await user.getFile()).text();
		}
	}

	const repo = new AuthRepository();
	const gateway = new Gateway();

	const connectionProfile = repo.getConnectionProfile();
	const wallet = repo.getWallet();
	const userId = repo.getUserId();

	async function submit() {
		const type = document.getElementById('field-type')?.innerText;
		const registration = document.getElementById('field-registration')?.innerText;
		const date = document.getElementById('field-date')?.innerText;
		const text = document.getElementById('field-text')?.innerText;
		if (![type, registration, date, text].every((val): val is string => val?.length)) {
			return;
		}
		await gateway.connect(await connectionProfile, {
			identity: await userId,
			wallet: await wallet,
			discovery: { enabled: true }
		});
		const net = await gateway.getNetwork(registration);
		const contract = net.getContract('doc');

		await contract.submitTransaction('CreateDoc', type, registration, date, text);
		gateway.disconnect();
	}
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" />
	<link
		rel="stylesheet"
		href="https://fonts.googleapis.com/css?family=Material+Icons&display=block"
	/>
</svelte:head>

<form class="form">
	<md-filled-text-field id="field-type" label="Type" />
	<md-filled-text-field id="field-registration" label="Registration" />
	<md-filled-text-field id="field-date" label="Date" />
	<md-filled-text-field id="field-text" label="Text" />
	<md-elevated-button label="Submit" on:click={submit} on:keypress={submit} />
</form>

<style>
	.form {
		color: white;
		display: flex;
		flex-direction: column;
	}
</style>
