
def get_cmd_to_get_raw_data(
    version: str,
    data_local_save_dir: str,
    dvc_remote_repo: str,
    dvc_data_folder: str,
    github_user_name: str,
    github_accesss_token: str
) -> None
    """
    Get shell command to donwload the raw data from dvc store
    """ 

    #dvc_remote_repo = "https://github.com/Rodrigo-Peres/cyberbullying-data-preparation.git"
    without_https = dvc_remote_repo.replace("https://", "") : str
    dvc_remote_repo = f"https://{github_user_name}:{github_accesss_token}@{without_https}"

    command = f"dvc get {dvc_remote_repo} {dvc_data_folder} --rev {version} -o {data_local_save_dir}"

    return command


def raw_data_with_version(
    version: str,
    data_local_save_dir: str,
    dvc_remote_repo: str,
    dvc_raw_data_folder: str,
    github_user_name: str,
    github_accesss_token: str
) -> None 

    command = get_cmd_to_get_raw_data(version, data_local_save_dir, dvc_remote_repo, dvc_raw_data_folder, github_user_name, github_accesss_token)