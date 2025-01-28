import duckdb


def get_conn(db_path: str) -> duckdb.DuckDBPyConnection:
    return duckdb.connect(db_path)


def init_qcew_table(db_path: str) -> None:
    conn = get_conn(db_path)
    conn.install_extension("spatial")
    conn.load_extension("spatial")
    conn.sql("DROP SEQUENCE IF EXISTS id_sequence;")
    conn.sql("CREATE SEQUENCE id_sequence START 1;")
    conn.sql(
        """
        CREATE TABLE IF NOT EXISTS "qcewtable" (
            id INTEGER PRIMARY KEY DEFAULT nextval('id_sequence'),
            trans_code TEXT,
            state_fips TEXT,
            year INTEGER,
            qtr INTEGER,
            ui_code TEXT,
            rep_uni_id TEXT,
            ein TEXT,
            pre_ui_code TEXT,
            pre_rep_uni_id TEXT,
            suc_ui_code TEXT,
            suc_rep_uni_id TEXT,
            leg_corp_name TEXT,
            trade_name TEXT,
            ui_str_addr_1 TEXT,
            ui_str_addr_2 TEXT,
            ui_addr_city TEXT,
            ui_addr_state TEXT,
            ui_addr_5_zip TEXT,
            ui_addr_zip_ext TEXT,
            phys_str_addr_1 TEXT,
            phys_str_addr_2 TEXT,
            phys_addr_city TEXT,
            phys_addr_state TEXT,
            phys_addr_5_zip TEXT,
            phys_addr_zip_ext TEXT,
            mail_str_addr_1 TEXT,
            mail_str_addr_2 TEXT,
            mail_addr_city TEXT,
            mail_addr_state TEXT,
            mail_addr_5_zip TEXT,
            mail_addr_zip_ext TEXT,
            mail_addr_type TEXT,
            rep_unit_desc TEXT,
            area_code TEXT,
            phone_prefix TEXT,
            phone_suffix TEXT,
            setup_date_year TEXT,
            setup_date_month TEXT,
            setup_date_day TEXT,
            init_liab_year TEXT,
            init_liab_month TEXT,
            init_liab_day TEXT,
            end_liab_year TEXT,
            end_liab_month TEXT,
            end_liab_day TEXT,
            reactivate_date_year TEXT,
            reactivate_date_month TEXT,
            reactivate_date_day TEXT,
            status_code TEXT,
            ces_indicator TEXT,
            ars_resp_code TEXT,
            ars_refile_year TEXT,
            old_country_code TEXT,
            old_own_code TEXT,
            ars_verif_code TEXT,
            old_town_code TEXT,
            max_rep_uni_num TEXT,
            mwr_mail_indicator TEXT,
            old_naics_code TEXT,
            data_source TEXT,
            special_indic_code TEXT,
            agent_code TEXT,
            sic_code TEXT,
            nsta_code TEXT,
            naics_code TEXT,
            own_code TEXT,
            org_type_code TEXT,
            counrty_code TEXT,
            town_code TEXT,
            aux_code TEXT,
            first_month_employment INTEGER,
            first_month_employment_indic TEXT,
            second_month_employment INTEGER,
            second_month_employment_indic TEXT,
            third_month_employment INTEGER,
            third_month_employment_indic TEXT,
            total_wages INTEGER,
            total_wages_indic TEXT,
            taxable_wages INTEGER,
            contributions_due TEXT,
            type_coverage_code TEXT,
            meei_code TEXT,
            report_change_indic TEXT,
            firt_comment TEXT,
            second_comment TEXT,
            third_comment TEXT,
            narrative_comment TEXT,
            collect_mod_indic TEXT,
            econ_code_change_indic TEXT,
            ui_addr_type TEXT,
            date_pla_change TEXT,
            geo_soft_a TEXT,
            geo_soft_b TEXT,
            match_code TEXT,
            loc_code TEXT,
            geom geometry,
            year_qtr_new_lat_long TEXT,
            place_code TEXT,
            class_code TEXT,
            census_block TEXT,
            census_tract TEXT,
            addr_cont TEXT,
            p_s_part_full_indic TEXT,
            p_s_transfer_year TEXT,
            p_s_transfer_month TEXT,
            p_s_transfer_day TEXT,
            mult_suc TEXT,
            mult_pre TEXT,
            pre_source_code TEXT,
            suc_source_code TEXT,
            first_suppl_pre_suc TEXT,
            second_suppl_pre_suc TEXT,
            ars_third_party_agent TEXT,
            phone_ext TEXT,
            qcew_contact TEXT,
            qcew_contact_title TEXT,
            qcew_contact_email TEXT,
            qcew_contact_fax TEXT,
            qcew_contact_website TEXT,
            future_use TEXT
            );
        """
    )


def init_hac_table(db_path: str) -> None:
    con = get_conn(db_path)
    con.sql("DROP SEQUENCE IF EXISTS id_sequence_hac;")
    con.sql("CREATE SEQUENCE id_sequence_hac START 1;")
    con.sql(
        """
    CREATE TABLE IF NOT EXISTS "hactable" (
    id INTEGER PRIMARY KEY DEFAULT nextval('id_sequence_hac'),
    SEM_NUM_PAT TEXT,
    SEM_HSEG_SOC TEXT,
    SEM_FORMA_LEGAL TEXT,
    SEM_NOMBRE TEXT,
    SEM_COD_ACTIVOS TEXT,
    SEM_SIC TEXT,
    SEM_INDUSTRIA TEXT,
    SEM_SIC_NEW TEXT,
    SEM_INDUSTRIA_N TEXT,
    NAICS_R02 TEXT,
    SEM_INDUS_R02 TEXT
    );
    """
    )


if __name__ == "__main__":
    con = get_conn("data.ddb")
    init_qcew_table("data.ddb")
