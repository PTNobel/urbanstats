import domtoimage from 'dom-to-image-more'
import { saveAs } from 'file-saver'
import React, { createContext, ReactNode, useContext } from 'react'

import { universe_path } from '../navigation/links'
import { Colors } from '../page_template/colors'

export function ScreenshotButton(props: { onClick: () => void }): ReactNode {
    const screencap_button = (
        <div
            onClick={props.onClick}
            style={{
                height: '100%',
                cursor: 'pointer',
            }}
        >
            <img src="/screenshot.png" alt="Screenshot Button" style={{ height: '100%' }} />
        </div>
    )
    // if screenshot mode is on, put a loading circle over the image
    if (useScreenshotMode()) {
        const pad = 10 // pct
        const loading_circle = (
            <div style={{
                position: 'absolute',
                height: `${100 - 2 * pad}%`,
                width: `${100 - 2 * pad}%`,
                top: `${pad}%`,
                left: `${pad}%`,
                borderRadius: '50%',
                border: '5px solid #fff',
                borderTop: '5px solid #000',
                animation: 'spin 2s linear infinite',
                zIndex: 2,
                animationPlayState: 'running',
            }}
            >
            </div>
        )
        const dim_filter = (
            <div style={{
                position: 'absolute',
                height: '100%',
                width: '100%',
                top: 0,
                left: 0,
                backgroundColor: 'rgba(0,0,0,0.5)',
                zIndex: 1,
            }}
            >
            </div>
        )
        return (
            <div style={{ position: 'relative', height: '100%', aspectRatio: '1/1' }}>
                {screencap_button}
                {dim_filter}
                {loading_circle}
            </div>
        )
    }
    return screencap_button
}

export interface ScreencapElements {
    path: string
    overall_width: number
    elements_to_render: HTMLElement[]
    height_multiplier?: number
}

export async function create_screenshot(config: ScreencapElements, universe: string | undefined, colors: Colors): Promise<void> {
    const overall_width = config.overall_width
    const height_multiplier = config.height_multiplier ?? 1

    async function screencap_element(ref: HTMLElement): Promise<[string, number]> {
        const scale_factor = overall_width / ref.offsetWidth
        const link = await domtoimage.toPng(ref, {
            bgcolor: colors.background,
            height: ref.offsetHeight * scale_factor * height_multiplier,
            width: ref.offsetWidth * scale_factor,
            style: {
                transform: `scale(${scale_factor})`,
                transformOrigin: 'top left',
            },
        })
        return [link, scale_factor * ref.offsetHeight * height_multiplier]
    }

    const png_links = []
    const heights = []
    for (const ref of config.elements_to_render) {
        try {
            const [png_link, height] = await screencap_element(ref)
            png_links.push(png_link)
            heights.push(height)
        }
        catch (e) {
            console.error(e)
        }
    }

    const canvas = document.createElement('canvas')

    const pad_around = 100
    const pad_between = 50

    const banner = new Image()
    await new Promise<void>((resolve) => {
        banner.onload = () => { resolve() }
        banner.src = '/screenshot_footer.svg'
    })

    const banner_scale = overall_width / banner.width
    const banner_height = banner.height * banner_scale

    canvas.width = pad_around * 2 + overall_width
    canvas.height = pad_around + pad_between * (png_links.length - 1) + heights.reduce((a, b) => a + b, 0) + banner_height

    const ctx = canvas.getContext('2d')!
    const imgs = []

    for (const png_link of png_links) {
        const img = new Image()
        img.src = png_link
        imgs.push(img)
    }
    ctx.fillStyle = colors.background
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    for (const img of imgs) {
        await new Promise<void>((resolve) => {
            img.onload = () => { resolve() }
        })
    }
    let start = pad_around
    for (const img of imgs) {
        ctx.drawImage(img, pad_around, start)
        start += img.height + pad_between
    }

    start -= pad_between

    ctx.drawImage(banner, pad_around, start, overall_width, banner_height)

    if (universe !== undefined) {
        const flag = new Image()
        flag.src = universe_path(universe)
        await new Promise<void>((resolve) => {
            flag.onload = () => { resolve() }
        })
        // draw on bottom left, same height as banner
        const flag_height = banner_height / 2
        const offset = flag_height / 2
        const flag_width = flag.width * flag_height / flag.height
        ctx.drawImage(flag, pad_around + offset, start + offset, flag_width, flag_height)
    }

    canvas.toBlob(function (blob) {
        saveAs(blob!, config.path)
    })
}

export const ScreenshotContext = createContext(false)

export function useScreenshotMode(): boolean {
    return useContext(ScreenshotContext)
}
