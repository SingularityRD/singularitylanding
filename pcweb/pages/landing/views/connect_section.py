import reflex as rx
import reflex_ui as ui

from pcweb.components.icons.icons import get_icon
from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("DatabaseAddIcon", class_name="shrink-0"),
            rx.el.span("Data", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Ingest Security Telemetry",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Centralize logs and signals from every layer of your stack for holistic situational awareness.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def connect_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            get_icon(icon, class_name="shrink-0 !text-slate-9 size-5"),
            rx.el.span(title, class_name="text-sm font-medium text-slate-10"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.el.p(
            description,
            class_name="text-slate-12 text-base font-medium",
        ),
        class_name="flex flex-col gap-4 p-10 border-r border-slate-3 border-b",
    )


def connect_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", class_name="left-0 top-0"),
            numbers_pattern(side="right", class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full relative overflow-hidden py-20 border-b border-slate-3 lg:border-x",
        ),
        rx.el.div(
            connect_card(
                "api",
                "IoT Sensors & Actuators",
                "Monitor voltage, temperature, and signal integrity directly from hardware.",
            ),
            connect_card(
                "python",
                "Edge Computing Nodes",
                "Secure data processing at the source with lightweight agents.",
            ),
            connect_card(
                "db",
                "Legacy & Modern IT",
                "Bridge the gap between vintage mainframes and modern cloud infrastructures.",
            ),
            connect_card(
                "doc",
                "Unstructured Logs",
                "Parse and analyze raw log files from diverse systems for anomaly detection.",
            ),
            class_name="w-full grid grid-cols-1 lg:grid-cols-2 lg:border-l border-slate-3",
        ),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] relative overflow-hidden",
    )
